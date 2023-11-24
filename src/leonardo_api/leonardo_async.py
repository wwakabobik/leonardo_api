# -*- coding: utf-8 -*-
"""
Filename: leonardo_async.py
Author: Iliya Vereshchagin
Copyright (c) 2023. All rights reserved.

Created: 28.08.2023
Last Modified: 24.11.2023

Description:
This file contains asynchronous implementation for Leonardo.ai API
"""

import json
import logging
import mimetypes
import os
from typing import Optional

import asyncio
import aiofiles
import aiohttp


from .logger_config import setup_logger


class Leonardo:
    """
    This class is for managing and interacting with Leonardo.ai service using async libraries.

    Parameters:
    auth_token (str): Auth Bearer token. Required.
    logger (logging.Logger, optional): default logger. Default will be initialized if not provided.
    """

    def __init__(self, auth_token: str, logger: Optional[logging.Logger] = None) -> None:
        """
        Constructs all the necessary attributes for the Leonardo object.

        :param auth_token: Auth Bearer token. Required.
        :type auth_token: str
        :param logger: default logger. Default will be initialized if not provided.
        :type logger: logging.Logger, optional
        """
        self.___auth_token = auth_token
        self.___logger = logger if logger else setup_logger("Leonardo", "leonardo_async.log")
        self.___logger.debug("Leonardo init complete")

    async def ___get_client_session(self, request_type: str = "get", empty: bool = False) -> aiohttp.ClientSession:
        """
        This method returns aiohttp.ClientSession with headers.

        :param request_type: type of request: "get" or "post"
        :type request_type: str
        :param empty: is True if headers will be empty
        :type empty: bool
        :return: client session with headers
        :rtype: aiohttp.ClientSession
        """
        headers = {}
        if not empty:
            headers = {"Authorization": f"Bearer {self.___auth_token}"}
            if request_type.lower() == "get" or request_type.lower() == "delete":
                headers.update({"content-type": "application/json"})
            if request_type.lower() == "post":
                headers.update({"accept": "application/json", "content-type": "application/json"})
        return aiohttp.ClientSession(headers=headers)

    async def get_user_info(self) -> dict:
        """
        This endpoint will return your user information, including your user ID.

        :return: user info
        :rtype: dict

        Raises:
            Exception: if error occurred while getting user info
        """
        url = "https://cloud.leonardo.ai/api/rest/v1/me"

        self.___logger.debug(f"Requesting user info: GET {url}")
        session = await self.___get_client_session("get")
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                response_dict = await response.json()
                self.___logger.debug(f"User info: {response_dict}")
                await session.close()
                return response_dict
        except Exception as error:
            self.___logger.error(f"Error occurred while getting user info: {str(error)}")
            if not session.closed:
                await session.close()
            raise error

    async def post_generations(
        self,
        prompt: str,
        negative_prompt: Optional[str] = None,
        model_id: Optional[str] = None,
        sd_version: Optional[str] = None,
        num_images: int = 4,
        width: int = 512,
        height: int = 512,
        num_inference_steps: int = 40,
        guidance_scale: int = 7,
        init_generation_image_id: Optional[str] = None,
        init_image_id: Optional[str] = None,
        init_strength: Optional[float] = None,
        scheduler: Optional[str] = None,
        preset_style: Optional[str] = None,
        tiling: bool = False,
        public: bool = False,
        prompt_magic: bool = True,
        control_net: bool = False,
        control_net_type: Optional[str] = None,
    ) -> dict:
        """
        This endpoint will generate images.

        :param prompt: The prompt used to generate images.
        :type prompt: str
        :param negative_prompt: The negative prompt used for the image generation.
        :type negative_prompt: str, optional
        :param model_id: The model ID used for the image generation.
        :type model_id: str, optional
        :param sd_version: The base version of stable diffusion to use if not using a custom model.
        :type sd_version: str, optional
        :param num_images: The number of images to generate. Default is 4.
        :type num_images: int, optional
        :param width: The width of the images. Default is 512px.
        :type width: int, optional
        :param height: The height of the images. Default is 512px.
        :type height: int, optional
        :param num_inference_steps: The number of inference steps for generation. Must be from 40 to 60. Default is 40.
        :type num_inference_steps: int, optional
        :param guidance_scale: How strongly the generation should reflect the prompt. Number from 1 to 20. Default is 7.
        :type guidance_scale: int, optional
        :param init_generation_image_id: The ID of an existing image to use in image2image.
        :type init_generation_image_id: str, optional
        :param init_image_id: The ID of an Init Image to use in image2image.
        :type init_image_id: str, optional
        :param init_strength: How strongly the generated images should reflect the original image in image2image.
        :type init_strength: float, optional
        :param scheduler: The scheduler to generate images with.
        :type scheduler: str, optional
        :param preset_style: The style to generate images with.
        :type preset_style: str, optional
        :param tiling: Whether the generated images should tile on all axis. Default is False.
        :type tiling: bool, optional
        :param public: Whether the generated images should show in the community feed. Default is False.
        :type public: bool, optional
        :param prompt_magic: Enable to use Prompt Magic. Default is True.
        :type prompt_magic: bool, optional
        :param control_net: Enable to use ControlNet. Requires an init image to be provided.
                            Requires a model based on SD v1.5. Default is False.
        :type control_net: bool, optional
        :param control_net_type: The type of ControlNet to use.
        :type control_net_type: str, optional
        :return: generation response
        :rtype: dict

        Raises:
            Exception: if error occurred while post generations
        """
        # pylint: disable=too-many-locals
        url = "https://cloud.leonardo.ai/api/rest/v1/generations"
        payload = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "modelId": model_id,
            "sd_version": sd_version,
            "num_images": num_images,
            "width": width,
            "height": height,
            "num_inference_steps": num_inference_steps,
            "guidance_scale": guidance_scale,
            "init_generation_image_id": init_generation_image_id,
            "init_image_id": init_image_id,
            "init_strength": init_strength,
            "scheduler": scheduler,
            "presetStyle": preset_style,
            "tiling": tiling,
            "public": public,
            "promptMagic": prompt_magic,
            "controlNet": control_net,
            "controlNetType": control_net_type,
        }
        self.___logger.debug(f"Requesting post generations: POST {url} with payload: {payload}")
        session = await self.___get_client_session("post")
        try:
            async with session.post(url, json=payload) as response:
                response.raise_for_status()
                response_dict = await response.json()
                self.___logger.debug(f"Post generations: {response_dict}")
                await session.close()
                return response_dict
        except Exception as error:
            self.___logger.error(f"Error occurred while post generations: {str(error)}")
            if not session.closed:
                await session.close()
            raise error

    async def get_single_generation(self, generation_id: str) -> dict:
        """
        This endpoint will provide information about a specific generation.

        :param generation_id: The ID of the generation to return.
        :type generation_id: str
        :return: generation info
        :rtype: dict

        Raises:
            Exception: if error occurred while get single generation
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/generations/{generation_id}"
        self.___logger.debug(f"Requested single generations: GET {url} with generation_id={generation_id}")
        session = await self.___get_client_session("get")
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                response_dict = await response.json()
                self.___logger.debug(f"Single generations: {response}")
                await session.close()
                return response_dict
        except Exception as error:
            self.___logger.error(f"Error occurred while get single generations: {str(error)}")
            if not session.closed:
                await session.close()
            raise

    async def delete_single_generation(self, generation_id: str) -> aiohttp.ClientResponse:
        """
        This endpoint deletes a specific generation.

        :param generation_id: The ID of the generation to delete.
        :type generation_id: str
        :return: generation info
        :rtype: aiohttp.ClientResponse

        Raises:
            Exception: if error occurred while delete single generation
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/generations/{generation_id}"
        self.___logger.debug(f"Delete generations with generation_id={generation_id}: DELETE {url}")
        session = await self.___get_client_session("delete")
        try:
            async with session.delete(url) as response:
                response.raise_for_status()
                self.___logger.debug(f"Generations {generation_id} has been deleted: {response}")
                await session.close()
                return response
        except Exception as error:
            self.___logger.error(f"Error occurred while delete generation: {str(error)}")
            if not session.closed:
                await session.close()
            raise error

    async def get_generations_by_user(self, user_id: str, offset: int = 0, limit: int = 10) -> dict:
        """
        This endpoint returns all generations by a specific user.

        :param user_id: The ID of the user.
        :type user_id: str
        :param offset: The offset for pagination.
        :type offset: int
        :param limit: The limit for pagination.
        :type limit: int
        :return: generations
        :rtype: dict

        Raises:
            Exception: if error occurred while get generations by user
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/generations/user/{user_id}"
        params = {"offset": offset, "limit": limit}
        self.___logger.debug(f"Requested generations for {user_id} with params {params}: GET {url}")
        session = await self.___get_client_session("get")
        try:
            async with session.get(url, params=params) as response:
                response.raise_for_status()
                response_dict = await response.json()
                self.___logger.debug(f"Generations for user {user_id} are: {response_dict}")
                await session.close()
                return response_dict
        except Exception as error:
            self.___logger.error(f"Error occurred while obtaining user's generations: {str(error)}")
            if not session.closed:
                await session.close()
            raise error

    async def upload_init_image(self, file_path: str) -> str:  # pylint: disable=too-many-locals
        """
        This endpoint returns pre-signed details to upload an init image to S3.

        :param file_path: The path to the image file.
        :type file_path: str
        :return: generation_id
        :rtype: str

        Raises:
            ValueError: if invalid file extension
            Exception: if error occurred while upload init image
        """
        valid_extensions = ["png", "jpg", "jpeg", "webp"]
        extension = os.path.splitext(file_path)[1].strip(".")
        if extension not in valid_extensions:
            raise ValueError(f"Invalid file extension. Must be one of {valid_extensions}")

        url = "https://cloud.leonardo.ai/api/rest/v1/init-image"
        payload = {"extension": extension}
        self.___logger.debug(f"Init image {file_path} upload requested with payload = {payload}: POST {url}")
        session = await self.___get_client_session("post")
        try:
            async with session.post(url, json=payload) as response:
                response.raise_for_status()
                data = await response.json()
                await session.close()
            self.___logger.debug(f"Init image {file_path} initiated as: {data['uploadInitImage']['url']}")
            generation_id = data["uploadInitImage"]["id"]
            upload_url = data["uploadInitImage"]["url"]
            fields = json.loads(data["uploadInitImage"]["fields"])

            self.___logger.debug(f"Init image {file_path} uploading with as binary: POST {upload_url}")
            async with aiofiles.open(file_path, "rb") as file:
                file_data = await file.read()
                data = aiohttp.FormData()
                for key, value in fields.items():
                    data.add_field(key, value)
                data.add_field("file", file_data, filename=file_path, content_type=mimetypes.guess_type(file_path)[0])
                session = await self.___get_client_session("post", empty=True)
                async with session.post(upload_url, data=data) as response:
                    response.raise_for_status()
                    self.___logger.debug(f"Init image {file_path} has been uploaded, generation_id is: {generation_id}")
                    await session.close()
                    return generation_id
        except Exception as error:
            self.___logger.error(f"Error occurred while upload init image: {str(error)}")
            if not session.closed:
                await session.close()
            raise error

    async def get_single_init_image(self, image_id: str) -> dict:
        """
        This endpoint will return a single init image.

        :param image_id: The ID of the init image to return.
        :type image_id: str
        :return: init image
        :rtype: dict

        Raises:
            Exception: if error occurred while get single init image
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/init-image/{image_id}"
        self.___logger.debug(f"Requested single image with image_id={image_id}: GET {url}")
        session = await self.___get_client_session("get")
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                response_dict = await response.json()
                self.___logger.debug(f"Single image provided: {response_dict}")
                await session.close()
                return response_dict
        except Exception as error:
            self.___logger.error(f"Error occurred while obtain single init image: {str(error)}")
            if not session.closed:
                await session.close()
            raise

    async def delete_init_image(self, image_id: str) -> aiohttp.ClientResponse:
        """
        This endpoint deletes an init image.

        :param image_id: The ID of the init image to delete.
        :type image_id: str
        :return: init image
        :rtype: aiohttp.ClientResponse

        Raises:
            Exception: if error occurred while delete init image
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/init-image/{image_id}"
        self.___logger.debug(f"Requested to delete single image with image_id={image_id}: DELETE {url}")
        session = await self.___get_client_session("delete")
        try:
            async with session.delete(url) as response:
                response.raise_for_status()
                self.___logger.debug(f"Single image deleted: {response}")
                await session.close()
                return response
        except Exception as error:
            self.___logger.error(f"Error occurred while deleting init image: {str(error)}")
            if not session.closed:
                await session.close()
            raise error

    async def create_upscale(self, image_id: str) -> aiohttp.ClientResponse:
        """
        This endpoint will create an upscale for the provided image ID.

        :param image_id: The ID of the image to upscale.
        :type image_id: str
        :return: upscale info
        :rtype: dict

        Raises:
            Exception: if error occurred while create upscale
        """
        url = "https://cloud.leonardo.ai/api/rest/v1/variations/upscale"
        payload = {"id": image_id}
        self.___logger.debug(f"Requested to upscale image with payload {payload}: POST {url}")
        session = await self.___get_client_session("post")
        try:
            async with session.post(url, json=payload) as response:
                response.raise_for_status()
                response_dict = await response.json()
                self.___logger.debug(f"Upscale created: {response_dict}")
                await session.close()
                return response_dict
        except Exception as error:
            self.___logger.error(f"Error occurred while up-scaling image: {str(error)}")
            if not session.closed:
                await session.close()
            raise error

    async def get_variation_by_id(self, generation_id: str) -> dict:
        """
        This endpoint will get the variation by ID.

        :param generation_id: The ID of the variation to get.
        :type generation_id: str
        :return: variation info
        :rtype: dict

        Raises:
            Exception: if error occurred while get variation by id
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/variations/{generation_id}"
        self.___logger.debug(f"Requested to obtain variation by id {generation_id}: GET {url}")
        session = await self.___get_client_session("get")
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                response_dict = await response.json()
                self.___logger.debug(f"Get variation by ID: {response_dict}")
                await session.close()
                return response_dict
        except Exception as error:
            self.___logger.error(f"Error occurred while get variation by id: {str(error)}")
            if not session.closed:
                await session.close()
            raise error

    async def create_dataset(self, name: str, description: Optional[str] = None) -> aiohttp.ClientResponse:
        """
        This endpoint creates a new dataset.

        :param name: The name of the dataset.
        :type name: str
        :param description: A description for the dataset.
        :type description: str, optional
        :return: dataset info
        :rtype: aiohttp.ClientResponse

        Raises:
            Exception: if error occurred while create dataset
        """
        url = "https://cloud.leonardo.ai/api/rest/v1/datasets"
        payload = {"name": name, "description": description}
        self.___logger.debug(f"Requested to create dataset with payload {payload}: POST {url}")
        session = await self.___get_client_session("post")
        try:
            async with session.post(url, json=payload) as response:
                response.raise_for_status()
                self.___logger.debug(f"Dataset has been created: {response}")
                await session.close()
                return response
        except Exception as error:
            self.___logger.error(f"Error occurred while create dataset: {str(error)}")
            if not session.closed:
                await session.close()
            raise error

    async def get_dataset_by_id(self, dataset_id: str) -> dict:
        """
        This endpoint gets the specific dataset.

        :param dataset_id: The ID of the dataset to return.
        :type dataset_id: str
        :return: dataset info
        :rtype: dict

        Raises:
            Exception: if error occurred while get dataset by id
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/datasets/{dataset_id}"
        self.___logger.debug(f"Requested to obtain dataset dataset_id={dataset_id}: GET {url}")
        session = await self.___get_client_session("get")
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                response_dict = await response.json()
                self.___logger.debug(f"Dataset with dataset_id={dataset_id} provided: {response_dict}")
                await session.close()
                return response_dict
        except Exception as error:
            self.___logger.error(f"Error occurred while get dataset: {str(error)}")
            if not session.closed:
                await session.close()
            raise

    async def delete_dataset_by_id(self, dataset_id: str) -> aiohttp.ClientResponse:
        """
        This endpoint deletes the specific dataset.

        :param dataset_id: The ID of the dataset to delete.
        :type dataset_id: str
        :return: response
        :rtype: aiohttp.ClientResponse

        Raises:
            Exception: if error occurred while delete dataset by id
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/datasets/{dataset_id}"
        self.___logger.debug(f"Requested to delete dataset dataset_id={dataset_id}: DELETE {url}")
        session = await self.___get_client_session("delete")
        try:
            async with session.delete(url) as response:
                response.raise_for_status()
                self.___logger.debug(f"Dataset with dataset_id={dataset_id} has been deleted: {response}")
                await session.close()
                return response
        except Exception as error:
            self.___logger.error(f"Error occurred while delete dataset: {str(error)}")
            if not session.closed:
                await session.close()
            raise error

    async def upload_dataset_image(self, dataset_id: str, file_path: str) -> aiohttp.ClientResponse:
        """
        This endpoint returns pre-signed details to upload a dataset image to S3.

        :param dataset_id: The ID of the dataset to which the image will be uploaded.
        :type dataset_id: str
        :param file_path: The path to the image file.
        :type file_path: str
        :return: dataset info
        :rtype: aiohttp.ClientResponse

        Raises:
            ValueError: if invalid file extension
        """
        # pylint: disable=too-many-locals
        valid_extensions = ["png", "jpg", "jpeg", "webp"]
        extension = os.path.splitext(file_path)[1].strip(".")
        if extension not in valid_extensions:
            raise ValueError(f"Invalid file extension. Must be one of {valid_extensions}")

        url = f"https://cloud.leonardo.ai/api/rest/v1/datasets/{dataset_id}/upload"

        payload = {"extension": extension}
        self.___logger.debug(f"Requested to upload dataset_id={dataset_id} from {file_path}: POST {url}")
        session = await self.___get_client_session("post")
        try:
            async with session.post(url, json=payload) as response:
                response.raise_for_status()
                data = await response.json()
                await session.close()
            self.___logger.debug(
                f"Dataset with dataset_id={dataset_id} started to upload from {file_path} as "
                f"{data['uploadDatasetImage']['url']}"
            )
            upload_url = data["uploadDatasetImage"]["url"]
            fields = json.loads(data["uploadDatasetImage"]["fields"])

            self.___logger.debug(f"Uploading dataset_id={dataset_id} from {file_path}: POST {url}")
            async with aiofiles.open(file_path, "rb") as file:
                file_data = await file.read()
                data = aiohttp.FormData()
                for key, value in fields.items():
                    data.add_field(key, value)
                data.add_field("file", file_data, filename=file_path, content_type=mimetypes.guess_type(file_path)[0])
                session = await self.___get_client_session("post", empty=True)
                async with session.post(upload_url, data=fields) as response:
                    response.raise_for_status()
                    self.___logger.debug(f"Dataset with dataset_id={dataset_id} uploaded using {file_path}: {response}")
                    await session.close()
                    return response
        except Exception as error:
            self.___logger.error(f"Error occurred uploading dataset: {str(error)}")
            if not session.closed:
                await session.close()
            raise

    async def upload_generated_image_to_dataset(
        self, dataset_id: str, generated_image_id: str
    ) -> aiohttp.ClientResponse:
        """
        This endpoint will upload a previously generated image to the dataset.

        :param dataset_id: The ID of the dataset to upload the image to.
        :type dataset_id: str
        :param generated_image_id: The ID of the image to upload to the dataset.
        :type generated_image_id: str
        :return: dataset info
        :rtype: aiohttp.ClientResponse

        Raises:
            Exception: if error occurred while upload generated image to dataset
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/datasets/{dataset_id}/upload/gen"
        payload = {"generatedImageId": generated_image_id}
        self.___logger.debug(
            f"Requested to upload generated_image_id={generated_image_id} " f"to dataset_id={dataset_id}: POST {url}"
        )
        session = await self.___get_client_session("post")
        try:
            async with session.post(url, json=payload) as response:
                response.raise_for_status()
                self.___logger.debug(
                    f"Image with image_id={generated_image_id} has been uploaded to "
                    f"dataset_id={dataset_id}: {response}"
                )
                await session.close()
                return response
        except Exception as error:
            self.___logger.error(f"Error occurred while upload generated image to dataset: {str(error)}")
            if not session.closed:
                await session.close()
            raise

    async def train_custom_model(
        self,
        name: str,
        dataset_id: str,
        instance_prompt: str,
        description: Optional[str] = None,
        model_type: str = "GENERAL",
        nsfw: bool = False,
        resolution: int = 512,
        sd_version: Optional[str] = None,
        strength: str = "MEDIUM",
    ) -> aiohttp.ClientResponse:
        """
        This endpoint will train a new custom model.

        :param name: The name of the model.
        :type name: str
        :param description: The description of the model.
        :type description: str, optional
        :param dataset_id: The ID of the dataset to train the model on.
        :type dataset_id: str
        :param instance_prompt: The instance prompt to use during training.
        :type instance_prompt: str
        :param model_type: The category the most accurately reflects the model.
        :type model_type: str, optional
        :param nsfw: mark for NSFW model. Default is False.
        :type nsfw: bool, optional
        :param resolution: The resolution for training. Must be 512 or 768.
        :type resolution: int, optional
        :param sd_version: The base version of stable diffusion to use if not using a custom model.
        :type sd_version: str, optional
        :param strength: When training using the PIXEL_ART model type, this influences the training strength.
        :type strength: str, optional
        :return: dataset info
        :rtype: aiohttp.ClientResponse

        Raises:
            Exception: if error occurred while train custom model
        """
        # pylint: disable=too-many-locals
        url = "https://cloud.leonardo.ai/api/rest/v1/models"
        payload = {
            "name": name,
            "description": description,
            "datasetId": dataset_id,
            "instance_prompt": instance_prompt,
            "modelType": model_type,
            "nsfw": nsfw,
            "resolution": resolution,
            "sd_Version": sd_version,
            "strength": strength,
        }
        self.___logger.debug(f"Requested to train custom model with payload {payload}: POST {url}")
        session = await self.___get_client_session("post")
        try:
            async with session.post(url, json=payload) as response:
                response.raise_for_status()
                self.___logger.debug(f"Custom modal has been trained: {response}")
                await session.close()
                return response
        except Exception as error:
            self.___logger.error(f"Error training custom model: {str(error)}")
            if not session.closed:
                await session.close()
            raise error

    async def get_custom_model_by_id(self, model_id: str) -> dict:
        """
        This endpoint gets the specific custom model.

        :param model_id: The ID of the custom model to return.
        :type model_id: str
        :return: custom model info
        :rtype: dict

        Raises:
            Exception: if error occurred while get custom model by id
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/models/{model_id}"
        self.___logger.debug(f"Requested to obtain custom model by model_id={model_id}: GET {url}")
        session = await self.___get_client_session("get")
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                response_dict = await response.json()
                self.___logger.debug(f"Custom modal has been trained: {response_dict}")
                await session.close()
                return response_dict
        except Exception as error:
            self.___logger.error(f"Error obtaining custom model: {str(error)}")
            if not session.closed:
                await session.close()
            raise

    async def delete_custom_model_by_id(self, model_id: str) -> aiohttp.ClientResponse:
        """
        This endpoint will delete a specific custom model.

        :param model_id: The ID of the model to delete.
        :type model_id: aiohttp.ClientResponse
        :return: custom model info
        :rtype: aiohttp.ClientResponse

        Raises:
            Exception: if error occurred while delete custom model by id
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/models/{model_id}"
        self.___logger.debug(f"Requested to delete custom model by model_id={model_id}: GET {url}")
        session = await self.___get_client_session("delete")
        try:
            async with session.delete(url) as response:
                response.raise_for_status()
                self.___logger.debug(f"Custom modal has been deleted: {response}")
                await session.close()
                return response
        except Exception as error:
            self.___logger.error(f"Error delete custom model: {str(error)}")
            if not session.closed:
                await session.close()
            raise error

    async def wait_for_image_generation(
        self, generation_id: str, image_index: int = 0, poll_interval: int = 5, timeout: int = 120
    ) -> aiohttp.ClientResponse:
        """
        This method waits for the completion of image generation.

        :param generation_id: The ID of the generation to check.
        :type generation_id: str
        :param image_index: (Optional) The index of the specific image to wait for. Default is 0.
        :type image_index: int, optional
        :param poll_interval: (Optional) The time interval in seconds between each check. Default is 5 seconds.
        :type poll_interval: int, optional
        :param timeout: (Optional) Waiting timeout. Default is 120 seconds.
        :type timeout: int, optional
        :return: The completed image(s) once generation is complete.
        :rtype: aiohttp.ClientResponse
        :raises IndexError: If an invalid image_index is provided.
        :raises TimeoutError: If the image has not been generated in timeout seconds.

        Raises:
            TimeoutError: if image has not been generated in timeout seconds
            IndexError: if incorrect image index
        """
        timeout_counter = 0
        while True:
            response = await self.get_single_generation(generation_id)
            generation = response.get("generations_by_pk", {})
            status = generation.get("status")

            if status == "COMPLETE":
                images = generation.get("generated_images", [])
                if image_index is not None:
                    if len(images) <= image_index < 0:
                        raise IndexError("Incorrect image index")
                    return images[image_index]

            await asyncio.sleep(poll_interval)

            if timeout_counter >= (timeout / poll_interval):
                raise TimeoutError(f"Image has not been generated in {timeout} seconds")

            timeout_counter += 1
