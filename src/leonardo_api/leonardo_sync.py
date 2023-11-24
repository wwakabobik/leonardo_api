# -*- coding: utf-8 -*-
"""
Filename: leonardo_sync.py
Author: Iliya Vereshchagin
Copyright (c) 2023. All rights reserved.

Created: 29.08.2023
Last Modified: 24.11.2023

Description:
This file contains synchronous implementation for Leonardo.ai API
"""

import json
import logging
import os
import time
from typing import Optional

import requests

from .logger_config import setup_logger


class Leonardo:
    """
    This class is for managing and interacting with Leonardo.ai service using regular requests libraries.

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

    def ___get_client_session(self, request_type: str = "get", empty: bool = False) -> requests.Session:
        """
        This method returns requests.Session() with headers.

        :param request_type: type of request: "get" or "post"
        :type request_type: str
        :param empty: is True if headers will be empty
        :type empty: bool
        :return: client session with headers
        :rtype: requests.Session
        """
        headers = {}
        if not empty:
            headers = {"Authorization": f"Bearer {self.___auth_token}"}
            if request_type.lower() == "get" or request_type.lower() == "delete":
                headers.update({"content-type": "application/json"})
            if request_type.lower() == "post":
                headers.update({"accept": "application/json", "content-type": "application/json"})
        session = requests.Session()
        session.headers.update(headers)
        return session

    def get_user_info(self) -> dict:
        """
        This endpoint will return your user information, including your user ID.

        :return: The user information.
        :rtype: dict

        Raises:
            Exception: If an error occurs while getting user info.
        """
        url = "https://cloud.leonardo.ai/api/rest/v1/me"
        self.___logger.debug(f"Requesting user info: GET {url}")
        session = self.___get_client_session("get")
        try:
            response = session.get(url)
            response.raise_for_status()
            response_dict = response.json()
            self.___logger.debug(f"User info: {response_dict}")
            session.close()
            return response_dict
        except Exception as error:
            self.___logger.error(f"Error occurred while getting user info: {str(error)}")
            raise error

    def post_generations(
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
    ) -> requests.Response:
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
        :return: The generation response.
        :rtype: requests.Response
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
        session = self.___get_client_session("post")
        try:
            response = session.post(url, json=payload)
            response.raise_for_status()
            response_dict = response.json()
            self.___logger.debug(f"Post generations: {response_dict}")
            return response_dict
        except Exception as error:
            self.___logger.error(f"Error occurred while post generations: {str(error)}")
            raise error

    def get_single_generation(self, generation_id: str) -> dict:
        """
        This endpoint will provide information about a specific generation.

        :param generation_id: The ID of the generation to return.
        :type generation_id: str
        :return: The generation information.
        :rtype: dict

        Raises:
            Exception: If an error occurs while getting generation info.
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/generations/{generation_id}"
        self.___logger.debug(f"Requested single generations: GET {url} with generation_id={generation_id}")
        session = self.___get_client_session("get")
        try:
            response = session.get(url)
            response.raise_for_status()
            response_dict = response.json()
            self.___logger.debug(f"Single generations: {response_dict}")
            return response_dict
        except Exception as error:
            self.___logger.error(f"Error occurred while get single generations: {str(error)}")
            raise error

    def delete_single_generation(self, generation_id: str) -> requests.Response:
        """
        This endpoint deletes a specific generation.

        :param generation_id: The ID of the generation to delete.
        :type generation_id: str
        :return: The response from the delete request.
        :rtype: requests.Response

        Raises:
            Exception: If an error occurs while deleting generation.
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/generations/{generation_id}"
        self.___logger.debug(f"Delete generations with generation_id={generation_id}: DELETE {url}")
        session = self.___get_client_session("delete")
        try:
            response = session.delete(url)
            response.raise_for_status()
            self.___logger.debug(f"Generations {generation_id} has been deleted: {response}")
            return response
        except Exception as error:
            self.___logger.error(f"Error occurred while delete generation: {str(error)}")
            raise error

    def get_generations_by_user(self, user_id: str, offset: int = 0, limit: int = 10) -> dict:
        """
        This endpoint returns all generations by a specific user.

        :param user_id: The ID of the user.
        :type user_id: str
        :param offset: The offset for pagination.
        :type offset: int
        :param limit: The limit for pagination.
        :type limit: int
        :return: The generations for the user.
        :rtype: dict

        Raises:
            Exception: If an error occurs while obtaining user's generations.
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/generations/user/{user_id}"
        params = {"offset": offset, "limit": limit}
        self.___logger.debug(f"Requested generations for {user_id} with params {params}: GET {url}")
        session = self.___get_client_session("get")
        try:
            response = session.get(url, params=params)
            response.raise_for_status()
            response_dict = response.json()
            self.___logger.debug(f"Generations for user {user_id} are: {response}")
            return response_dict
        except Exception as error:
            self.___logger.error(f"Error occurred while obtaining user's generations: {str(error)}")
            raise error

    def upload_init_image(self, file_path: str) -> str:
        """
        This endpoint returns pre-signed details to upload an init image to S3.

        :param file_path: The path to the image file.
        :type: str
        :return: The generation ID of the uploaded image.
        :rtype: str
        :raises ValueError: If an invalid file extension is provided.

        Raises:
            ValueError: If an invalid file extension is provided.
            Exception: If an error occurs while uploading the image.
        """
        valid_extensions = ["png", "jpg", "jpeg", "webp"]
        extension = os.path.splitext(file_path)[1].strip(".")
        if extension not in valid_extensions:
            raise ValueError(f"Invalid file extension. Must be one of {valid_extensions}")

        url = "https://cloud.leonardo.ai/api/rest/v1/init-image"
        payload = {"extension": extension}
        self.___logger.debug(f"Init image {file_path} upload requested with payload = {payload}: POST {url}")
        session = self.___get_client_session("post")
        try:
            response = session.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            self.___logger.debug(f"Init image {file_path} initiated: {data}")
            upload_url = data["uploadInitImage"]["url"]
            fields = json.loads(data["uploadInitImage"]["fields"])
            generation_id = data["uploadInitImage"]["id"]
            session.close()

            self.___logger.debug(f"Init image {file_path} uploading as binary: POST {upload_url}")
            session = self.___get_client_session("post", empty=True)
            with open(file_path, "rb") as file:
                file_data = file.read()
                fields.update({"file": file_data})
                response = session.post(upload_url, data=fields)
                response.raise_for_status()
                self.___logger.debug(f"Init image {file_path} has been uploaded with generation_id={generation_id}")
                return generation_id
        except Exception as error:
            self.___logger.error(f"Error occurred while upload init image: {str(error)}")
            raise error

    def get_single_init_image(self, image_id: str) -> dict:
        """
        This endpoint will return a single init image.

        :param image_id: The ID of the init image to return.
        :type image_id: str
        :return: The init image.
        :rtype: dict
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/init-image/{image_id}"
        self.___logger.debug(f"Requested single image with image_id={image_id}: GET {url}")
        session = self.___get_client_session("get")
        try:
            response = session.get(url)
            response.raise_for_status()
            response_dict = response.json()
            self.___logger.debug(f"Single image provided: {response_dict}")
            return response_dict
        except Exception as error:
            self.___logger.error(f"Error occurred while obtain single init image: {str(error)}")
            raise error

    def delete_init_image(self, image_id: str) -> requests.Response:
        """
        This endpoint deletes an init image.

        :param image_id: The ID of the init image to delete.
        :type image_id: str
        :return: The response from the delete request.
        :rtype: requests.Response

        Raises:
            Exception: If an error occurs while deleting init image.
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/init-image/{image_id}"
        self.___logger.debug(f"Requested to delete single image with image_id={image_id}: DELETE {url}")
        session = self.___get_client_session("delete")
        try:
            response = session.delete(url)
            response.raise_for_status()
            self.___logger.debug(f"Single image deleted: {response}")
            session.close()
            return response
        except Exception as error:
            self.___logger.error(f"Error occurred while deleting init image: {str(error)}")
            raise error

    def create_upscale(self, image_id: str) -> requests.Response:
        """
        This endpoint will create an upscale for the provided image ID.

        :param image_id: The ID of the image to upscale.
        :type image_id: str
        :return: The response from the create request.
        :rtype: requests.Response

        Raises:
            Exception: If an error occurs while creating upscale.
        """
        url = "https://cloud.leonardo.ai/api/rest/v1/variations/upscale"
        payload = {"id": image_id}
        self.___logger.debug(f"Requested to upscale image with payload {payload}: POST {url}")
        session = self.___get_client_session("post")
        try:
            response = session.post(url, json=payload)
            response.raise_for_status()
            self.___logger.debug(f"Upscale created: {response}")
            session.close()
            return response
        except Exception as error:
            self.___logger.error(f"Error occurred while up-scaling image: {str(error)}")
            raise error

    def get_variation_by_id(self, generation_id: str) -> requests.Response:
        """
        This endpoint will get the variation by ID.

        :param generation_id: The ID of the variation to get.
        :type generation_id: str
        :return: The variation.
        :rtype: requests.Response

        Raises:
            Exception: If an error occurs while getting variation.
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/variations/{generation_id}"
        self.___logger.debug(f"Requested to obtain variation by id {generation_id}: GET {url}")
        session = self.___get_client_session("get")
        try:
            response = session.get(url)
            response.raise_for_status()
            response_dict = response.json()
            self.___logger.debug(f"Get variation by ID: {response_dict}")
            return response_dict
        except Exception as error:
            self.___logger.error(f"Error occurred while get variation by id: {str(error)}")
            raise error

    def create_dataset(self, name: str, description: Optional[str] = None) -> requests.Response:
        """
        This endpoint creates a new dataset.

        :param name: The name of the dataset.
        :type name: str
        :param description: A description for the dataset.
        :type description: str, optional
        :return: The response from the create request.
        :rtype: requests.Response

        Raises:
            Exception: If an error occurs while creating dataset.
        """
        url = "https://cloud.leonardo.ai/api/rest/v1/datasets"
        payload = {"name": name, "description": description}
        self.___logger.debug(f"Requested to create dataset with payload {payload}: POST {url}")
        session = self.___get_client_session("post")
        try:
            response = session.post(url, json=payload)
            response.raise_for_status()
            self.___logger.debug(f"Dataset has been created: {response}")
            session.close()
            return response
        except Exception as error:
            self.___logger.error(f"Error occurred while create dataset: {str(error)}")
            raise error

    def get_dataset_by_id(self, dataset_id: str) -> dict:
        """
        This endpoint gets the specific dataset.

        :param dataset_id: The ID of the dataset to return.
        :type dataset_id: str
        :return: The dataset.
        :rtype: dict

        Raises:
            Exception: If an error occurs while getting dataset.
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/datasets/{dataset_id}"
        self.___logger.debug(f"Requested to obtain dataset dataset_id={dataset_id}: GET {url}")
        session = self.___get_client_session("get")
        try:
            response = session.get(url)
            response.raise_for_status()
            response_dict = response.json()
            self.___logger.debug(f"Dataset with dataset_id={dataset_id} provided: {response_dict}")
            return response_dict
        except Exception as error:
            self.___logger.error(f"Error occurred while get dataset: {str(error)}")
            raise error

    def delete_dataset_by_id(self, dataset_id: str) -> requests.Response:
        """
        This endpoint deletes the specific dataset.

        :param dataset_id: The ID of the dataset to delete.
        :type dataset_id: str
        :return: The response from the delete request.
        :rtype: requests.Response

        Raises:
            Exception: If an error occurs while deleting dataset.
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/datasets/{dataset_id}"
        self.___logger.debug(f"Requested to delete dataset dataset_id={dataset_id}: DELETE {url}")
        session = self.___get_client_session("delete")
        try:
            response = session.delete(url)
            response.raise_for_status()
            self.___logger.debug(f"Dataset with dataset_id={dataset_id} has been deleted: {response}")
            return response
        except Exception as error:
            self.___logger.error(f"Error occurred while delete dataset: {str(error)}")
            raise error

    def upload_dataset_image(self, dataset_id: str, file_path: str) -> requests.Response:
        """
        This endpoint returns pre-signed details to upload a dataset image to S3.

        :param dataset_id: The ID of the dataset to which the image will be uploaded.
        :type dataset_id: str
        :param file_path: The path to the image file.
        :type file_path: str
        :return: The response from the upload request.
        :rtype: requests.Response

        Raises:
            ValueError: If an invalid file extension is provided.
        """
        # pylint: disable=too-many-locals
        valid_extensions = ["png", "jpg", "jpeg", "webp"]
        extension = os.path.splitext(file_path)[1].strip(".")
        if extension not in valid_extensions:
            raise ValueError(f"Invalid file extension. Must be one of {valid_extensions}")

        url = f"https://cloud.leonardo.ai/api/rest/v1/datasets/{dataset_id}/upload"

        payload = {"extension": extension}
        self.___logger.debug(f"Requested to upload dataset_id={dataset_id} from {file_path}: POST {url}")
        session = self.___get_client_session("post")
        try:
            response = session.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            self.___logger.debug(
                f"Dataset with dataset_id={dataset_id} started to upload from {file_path}:" f" {response}"
            )
            upload_url = data["uploadDatasetImage"]["url"]
            fields = json.loads(data["uploadDatasetImage"]["fields"])
            dataset_id = data["uploadDatasetImage"]["datasetId"]

            self.___logger.debug(f"Uploading dataset_id={dataset_id} from {file_path}: POST {url}")
            session = self.___get_client_session("post", empty=True)
            with open(file_path, "rb") as file:
                file_data = file.read()
                fields.update({"file": file_data})
                response = session.post(upload_url, data=fields)
                response.raise_for_status()
                self.___logger.debug(f"Dataset with dataset_id={dataset_id} uploaded using {file_path}")
                session.close()
                return response
        except Exception as error:
            self.___logger.error(f"Error occurred uploading dataset: {str(error)}")
            raise error

    def upload_generated_image_to_dataset(self, dataset_id: str, generated_image_id: str) -> requests.Response:
        """
        This endpoint will upload a previously generated image to the dataset.

        :param dataset_id: The ID of the dataset to upload the image to.
        :type dataset_id: str
        :param generated_image_id: The ID of the image to upload to the dataset.
        :type generated_image_id: str
        :return: The response from the upload request.
        :rtype: requests.Response

        Raises:
            Exception: If an error occurs while uploading image to dataset.
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/datasets/{dataset_id}/upload/gen"
        payload = {"generatedImageId": generated_image_id}
        self.___logger.debug(
            f"Requested to upload generated_image_id={generated_image_id} " f"to dataset_id={dataset_id}: POST {url}"
        )
        session = self.___get_client_session("post")
        try:
            response = session.post(url, json=payload)
            response.raise_for_status()
            self.___logger.debug(
                f"Image with image_id={generated_image_id} has been uploaded to " f"dataset_id={dataset_id}: {response}"
            )
            session.close()
            return response
        except Exception as error:
            self.___logger.error(f"Error occurred while upload generated image to dataset: {str(error)}")
            raise error

    def train_custom_model(
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
    ) -> requests.Response:
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
        :type model_type: str
        :param nsfw: mark for NSFW model. Default is False.
        :type nsfw: bool, optional
        :param resolution: The resolution for training. Must be 512 or 768.
        :type resolution: int, optional
        :param sd_version: The base version of stable diffusion to use if not using a custom model.
        :type sd_version: str, optional
        :param strength: When training using the PIXEL_ART model type, this influences the training strength.
        :type strength: str, optional
        :return: The response from the create request.
        :rtype: requests.Response
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
        session = self.___get_client_session("post")
        try:
            response = session.post(url, json=payload)
            response.raise_for_status()
            self.___logger.debug(f"Custom modal has been trained: {response}")
            session.close()
            return response
        except Exception as error:
            self.___logger.error(f"Error training custom model: {str(error)}")
            raise error

    def get_custom_model_by_id(self, model_id: str) -> dict:
        """
        This endpoint gets the specific custom model.

        :param model_id: The ID of the custom model to return.
        :type model_id: str
        :return: The custom model.
        :rtype: dict

        Raises:
            Exception: If an error occurs while getting custom model.
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/models/{model_id}"
        self.___logger.debug(f"Requested to obtain custom model by model_id={model_id}: GET {url}")
        session = self.___get_client_session("get")
        try:
            response = session.get(url)
            response.raise_for_status()
            response_dict = response.json()
            self.___logger.debug(f"Custom modal has been trained: {response_dict}")
            session.close()
            return response_dict
        except Exception as error:
            self.___logger.error(f"Error obtaining custom model: {str(error)}")
            raise error

    def delete_custom_model_by_id(self, model_id: str) -> requests.Response:
        """
        This endpoint will delete a specific custom model.

        :param model_id: The ID of the model to delete.
        :type model_id: str
        :return: The response from the delete request.
        :rtype: requests.Response

        Raises:
            Exception: If an error occurs while deleting custom model.
        """
        url = f"https://cloud.leonardo.ai/api/rest/v1/models/{model_id}"
        self.___logger.debug(f"Requested to delete custom model by model_id={model_id}: GET {url}")
        session = self.___get_client_session("delete")
        try:
            response = session.delete(url)
            response.raise_for_status()
            self.___logger.debug(f"Custom modal has been deleted: {response}")
            return response
        except Exception as error:
            self.___logger.error(f"Error delete custom model: {str(error)}")
            raise error

    def wait_for_image_generation(
        self, generation_id: str, image_index: int = 0, poll_interval: int = 5, timeout: int = 120
    ) -> requests.Response:
        """
        This method waits for the completion of image generation.

        :param generation_id: The ID of the generation to check.
        :type generation_id: str
        :param image_index: (Optional) The index of the specific image to wait for.
                                       If None, waits for all images to complete.
        :type image_index: int, optional
        :param poll_interval: (Optional) The time interval in seconds between each check. Default is 5 seconds.
        :type poll_interval: int, optional
        :param timeout: (Optional) Waiting timeout. Default is 120 seconds.
        :type timeout: int, optional
        :raises TimeoutError: If the image(s) have not been generated within the timeout.
        :raises IndexError: If an invalid image_index is provided.
        :return: The completed image(s) once generation is complete.
        :rtype: requests.Response

        Raises:
            TimeoutError: If the image(s) have not been generated within the timeout.
            IndexError: If an invalid image_index is provided.
        """
        timeout_counter = 0
        while True:
            response = self.get_single_generation(generation_id)
            generation = response.get("generations_by_pk", {})
            status = generation.get("status")

            if status == "COMPLETE":
                images = generation.get("generated_images", [])
                if image_index is not None:
                    if len(images) <= image_index < 0:
                        raise IndexError("Incorrect image index")
                    return images[image_index]

            time.sleep(poll_interval)

            if timeout_counter >= (timeout / poll_interval):
                raise TimeoutError(f"Image has not been generated in {timeout} seconds")

            timeout_counter += 1
