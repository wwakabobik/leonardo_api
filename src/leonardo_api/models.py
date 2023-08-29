# -*- coding: utf-8 -*-
"""
Filename: models.py
Author: Iliya Vereshchagin
Copyright (c) 2023. All rights reserved.

Created: 29.08.2023
Last Modified: 30.08.2023

Description:
This file contains dicts with lists of models, split by nsfw/sfw custom models and platform models
"""

# pylint: disable=too-many-lines
# pylint: disable=line-too-long
# flake8: noqa


nsfw_models = {
    "data": {
        "custom_models": [
            {
                "id": "95bf5c4a-2f7e-4585-9783-b312fc90f5aa",
                "name": "Eitan Klein ",
                "description": "This model is inspired by the photographer and Israeli artist Eitan Klein, who is involved in capturing the male model and specializes in exposure ...",
                "instancePrompt": "photography  by Eitan Klein",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-01T03:56:30.167",
                "sdVersion": "v2",
                "type": "CHARACTERS",
                "nsfw": True,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "a6ac57fc-1d99-4c25-bde7-71c2912fe2e9", "username": "tomtom10_1", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a man",
                        "generated_images": [
                            {
                                "id": "c379f001-f371-426e-ad1c-494069b59d26",
                                "url": "https://cdn.leonardo.ai/users/a6ac57fc-1d99-4c25-bde7-71c2912fe2e9/generations/8b5a1203-ae62-42db-bfcc-2bb09b11e575/Eitan_Klein_a_man_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "0b24aca5-012a-4340-826a-1bc56f46f1e4",
                "name": "Realistic Portraits - NSFW",
                "description": "Portrait imagery",
                "instancePrompt": "high-end portrait photography",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-02-10T02:43:10.395",
                "sdVersion": "v2",
                "type": "FASHION",
                "nsfw": True,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "26675562-66e5-4085-9f62-b80925f54ef9", "username": "Tango_one", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/26675562-66e5-4085-9f62-b80925f54ef9/generations/4e522de3-e6ff-4820-a00d-2f97008473e4/Realistic_Portraits_NSFW_photorealistic_body_photography_of_a_beautiful_girl_sitting_2.jpg",
                    "id": "01c0ad36-8730-4fbf-a76d-e15b82c093d5",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "RAW photo, 8k ultrasharp photoshoot, instagram, stunning college girl",
                        "generated_images": [
                            {
                                "id": "c8a86e5c-3e7c-4abb-8240-ef3cbc6c7004",
                                "url": "https://cdn.leonardo.ai/users/26675562-66e5-4085-9f62-b80925f54ef9/generations/639a85ef-a8a6-4b04-900c-ef74295b1c22/Realistic_Portraits_NSFW_RAW_photo_8k_ultrasharp_photoshoot_instagram_stunning_colle_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "63a10c3a-37fd-48a8-88ec-ca680fe08626",
                "name": "car beetle pickup truck ram",
                "description": "",
                "instancePrompt": "A car",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-02-09T20:54:17.222",
                "sdVersion": "v1_5",
                "type": "PRODUCT_DESIGN",
                "nsfw": True,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "a256dfb3-302d-45dd-810c-285af352258d", "username": "Ronalt", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "car",
                        "generated_images": [
                            {
                                "id": "7dc269d8-d26a-4fc3-80f6-794f6551fdd8",
                                "url": "https://cdn.leonardo.ai/users/cfb583d7-2b0a-44df-980c-8b09a4582b0f/generations/c7d3f0a8-9561-42e4-881f-0fd9e43c5ab2/car_beetle_pickup_truck_ram_car_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "7a54c523-b876-4bc0-9071-1119cabba6ab",
                "name": "Schiele",
                "description": "Egon Schiele art",
                "instancePrompt": "a young man in the style of Egon Schiele",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-02-05T18:27:06.242",
                "sdVersion": "v1_5",
                "type": "ILLUSTRATIONS",
                "nsfw": True,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "afd16662-7b51-4ad2-a1f5-ba24a021dc54", "username": "Izzyjim", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/afd16662-7b51-4ad2-a1f5-ba24a021dc54/generations/f7888a81-6853-4751-91e0-f50212549cc7/Schiele_portrait_of_a_mean_young_woman_in_the_style_of_Egon_S_1.jpg",
                    "id": "250644d2-05c2-445a-b847-355cded5aa7c",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a young man standing a corner of a cul de in the style of Egon Schiele",
                        "generated_images": [
                            {
                                "id": "6d06a436-cb1d-4591-84d3-6e794011d801",
                                "url": "https://cdn.leonardo.ai/users/afd16662-7b51-4ad2-a1f5-ba24a021dc54/generations/5e09ba42-a674-43dc-bf25-a7a72c3d7649/Schiele_a_young_man_standing_a_corner_of_a_cul_de_in_the_style_of_Ego_1.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "6ac1218f-52d5-4a02-80ca-7599a4b2d895",
                "name": "cenobites",
                "description": "Clive Barker's Cenobites",
                "instancePrompt": "a Cenobite",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-02-03T14:06:54.566",
                "sdVersion": "v2",
                "type": "CHARACTERS",
                "nsfw": True,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "afd16662-7b51-4ad2-a1f5-ba24a021dc54", "username": "Izzyjim", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/afd16662-7b51-4ad2-a1f5-ba24a021dc54/generations/33bd142b-d430-4bb9-894f-662c75ef5694/cenobites_A_naturalskinned_Cenobite_with_freckles_wearing_a_wh_1.jpg",
                    "id": "bb866f93-51c8-4360-858a-b292d509453a",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": " woman fronting camera open white shirt, fire brustings from between her breasts, dramatic seance, back lighting , studio lighting ",
                        "generated_images": [
                            {
                                "id": "d8983ee2-954b-4427-80fd-1d4c5264fbdf",
                                "url": "https://cdn.leonardo.ai/users/afd16662-7b51-4ad2-a1f5-ba24a021dc54/generations/1807743a-fa39-45fd-82d0-2679d4127894/cenobites_woman_fronting_camera_open_white_shirt_fire_brustings_from_b_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "72db3416-b7e0-46bf-83f0-ac2dccc44fd2",
                "name": "Grimdark",
                "description": "Grimdark, warhammer 40k, horus heresy",
                "instancePrompt": "warhammer",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-02-02T19:19:24.818",
                "sdVersion": "v2",
                "type": "ILLUSTRATIONS",
                "nsfw": True,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "a5bca136-5cb9-4cca-8fbf-bf13835a523a", "username": "visceral3d", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "spacemarine",
                        "generated_images": [
                            {
                                "id": "ae61c2ba-8ce0-4c86-9b58-6811cab8a636",
                                "url": "https://cdn.leonardo.ai/users/1a892409-c957-427a-8473-1f461b43cf09/generations/3c9dd566-898a-446c-aef1-8fa467e4a784/Grimdark_spacemarine_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "3a43f9bd-bb36-48ab-af07-cbd9c985a55b",
                "name": "Scarred and damaged/bandaged characters",
                "description": "a design for damaged characters that are slightly or heavily bandaged",
                "instancePrompt": "A Slightly Bandaged Scarred Character.",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-01-31T04:38:57.094",
                "sdVersion": "v2",
                "type": "CHARACTERS",
                "nsfw": True,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "e407c8d7-45a3-451f-b8cf-f39d86df2fa0",
                    "username": "ShopKeeperPyro",
                    "__typename": "users",
                },
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/e407c8d7-45a3-451f-b8cf-f39d86df2fa0/generations/02e14a68-dbe1-427f-bb14-d9f6d5fcfbab/Scarred_and_damagedbandaged_characters_A_Slightly_Bandaged_Scarred_CharacterFull_body_character_d_3.jpg",
                    "id": "887740ce-48bb-4807-98e2-e9dd9e69e1d4",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "steampunk full body portrait, male character design with a bandaged face",
                        "generated_images": [
                            {
                                "id": "cc601bfe-8d23-446d-a6a7-93a756855c57",
                                "url": "https://cdn.leonardo.ai/users/e407c8d7-45a3-451f-b8cf-f39d86df2fa0/generations/72aa748f-2f68-475d-9edc-59ad0fc0594c/Scarred_and_damagedbandaged_characters_steampunk_full_body_portrait_male_character_design_with_a_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "6b2fe263-b081-4b13-8cc1-04cdd2e1179f",
                "name": "Artificial Busts ",
                "description": "This is finetune of SD2.1 for generating realistic busts. Tuning upon CC0 images from MET New York and few other free resources. ",
                "instancePrompt": "A bust ",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-01-22T00:21:12.931",
                "sdVersion": "v2",
                "type": "GENERAL",
                "nsfw": True,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "6b0af8c4-7cd0-493f-82d3-ce5508dcdea8", "username": "rhizomuser", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": " A detailed bust of a mysterious figure, rendered in a surrealistic style.",
                        "generated_images": [
                            {
                                "id": "c4f0d816-d5fa-4673-bf6c-e29531796832",
                                "url": "https://cdn.leonardo.ai/users/6b0af8c4-7cd0-493f-82d3-ce5508dcdea8/generations/518a8b0d-e465-402b-b5c5-93a40612a881/Artificial_Bustes_A_detailed_bust_of_a_mysterious_figure_rendered_in_a_surrea_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "4136b90e-e16e-40de-ae8e-40f7313e6b91",
                "name": " neon night",
                "description": "bluish neon colors",
                "instancePrompt": "neon night",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-01-19T06:33:29.285",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": True,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "353533d4-c015-47d7-90be-199ddfddcd90", "username": "jaspior", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "neon night",
                        "generated_images": [
                            {
                                "id": "477ebda0-fc68-4048-8c04-cf05ee133567",
                                "url": "https://cdn.leonardo.ai/users/353533d4-c015-47d7-90be-199ddfddcd90/generations/4773e379-75de-46ce-bf69-85e12fb8f583/neon_night_neon_night_1.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "9af4f4a0-5c89-4458-b0a9-14d36208e24e",
                "name": "Airbrush Design",
                "description": "80s and 90s Airbrush Desing Style",
                "instancePrompt": "An Airbrush Painting",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-01-18T01:59:27.292",
                "sdVersion": "v2",
                "type": "ILLUSTRATIONS",
                "nsfw": True,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "019f0238-4481-4bc8-9789-759e481d2e4e", "username": "aiaiaiaiai", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/019f0238-4481-4bc8-9789-759e481d2e4e/generations/a67f9499-bfb2-4ab4-a99b-6e076e591c05/80s_and_90s_Airbrush_Paintings_and_Ads_An_airbrush_painting_of_Sneakers_0.jpg",
                    "id": "e37e564a-822f-422b-aba2-60ef4be21647",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "An airbrush painting of Sneakers",
                        "generated_images": [
                            {
                                "id": "e37e564a-822f-422b-aba2-60ef4be21647",
                                "url": "https://cdn.leonardo.ai/users/019f0238-4481-4bc8-9789-759e481d2e4e/generations/a67f9499-bfb2-4ab4-a99b-6e076e591c05/80s_and_90s_Airbrush_Paintings_and_Ads_An_airbrush_painting_of_Sneakers_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "be795181-644d-4010-abd7-ff45805931bd",
                "name": "macbass",
                "description": "Stylization based on a particluar french band...",
                "instancePrompt": "black and white doodle",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-01-17T01:31:22.187",
                "sdVersion": "v1_5",
                "type": "ILLUSTRATIONS",
                "nsfw": True,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "cbabf1d4-23c3-4bd8-a520-48c53cd0e626",
                    "username": "FoxBonesMulder",
                    "__typename": "users",
                },
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "Gorgeous tattooed woman riding a dolphin",
                        "generated_images": [
                            {
                                "id": "da1dd922-69ef-4b7e-85ea-25a3605b45a7",
                                "url": "https://cdn.leonardo.ai/users/cbabf1d4-23c3-4bd8-a520-48c53cd0e626/generations/cbb17167-5308-45e3-ab45-65b46c333d57/MacBass_Gorgeous_tattooed_woman_riding_a_dolphin_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "db02a078-a251-4858-b5c5-d9530f6a03a0",
                "name": "Pin-Up Ladies",
                "description": "Generate Pin-Up Styled Women!",
                "instancePrompt": "Pin-Up, Lingerie",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-01-15T01:53:37.047",
                "sdVersion": "v1_5",
                "type": "CHARACTERS",
                "nsfw": True,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "02a3d88b-3380-43d3-b28c-1350876851b9", "username": "LouCipher", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "Lace, Breasts, Blonde",
                        "generated_images": [
                            {
                                "id": "e29f1359-d757-4630-8262-4710255ec044",
                                "url": "https://cdn.leonardo.ai/users/02a3d88b-3380-43d3-b28c-1350876851b9/generations/31c1cfeb-5c22-49e8-90cc-52bd8d56a2b8/PinUp_Ladies_Lace_Breasts_Blonde_0.png",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "45cbd18f-877a-4f63-8226-86ab45eabc11",
                "name": "Kojima-Bot v2.1",
                "description": "Generate Hideo Kojima using v2.1!",
                "instancePrompt": "Hideo Kojima",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-01-14T22:10:14.504",
                "sdVersion": "v2",
                "type": "CHARACTERS",
                "nsfw": True,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "02a3d88b-3380-43d3-b28c-1350876851b9", "username": "LouCipher", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "kojima as a purple stuffed worm in flap jaw space with a tuning fork doing a raw blink on hara-kiri rock I need scissors! 61!",
                        "generated_images": [
                            {
                                "id": "98d28288-ae1f-4b48-ae8e-9690c9261ad9",
                                "url": "https://cdn.leonardo.ai/users/02a3d88b-3380-43d3-b28c-1350876851b9/generations/97b40102-1f0e-47a1-97ee-31773d05fdca/KojimaBot_v21_kojima_as_a_purple_stuffed_worm_in_flap_jaw_space_with_a_tun_0.png",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "b42069d2-4954-4ac9-a264-05177bf2484b",
                "name": '"Metal Gear" Style Characters',
                "description": "Generate characters inspired by the artwork of Yoji Shinkawa.",
                "instancePrompt": "drawn by Yoji Shinkawa",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-01-14T18:46:36.17",
                "sdVersion": "v1_5",
                "type": "CHARACTERS",
                "nsfw": True,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "02a3d88b-3380-43d3-b28c-1350876851b9", "username": "LouCipher", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "Hideo Kojima",
                        "generated_images": [
                            {
                                "id": "7abfecfe-99ee-412e-981c-1eed7f69607b",
                                "url": "https://cdn.leonardo.ai/users/02a3d88b-3380-43d3-b28c-1350876851b9/generations/c3d4e247-319a-4d0d-b15e-f38bf6ff0d7f/Metal_Gear_Style_Characters_Hideo_Kojima_0.png",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "30e15b51-dbf2-4c70-9281-ba4c659e795b",
                "name": "Borderland Style",
                "description": "Borderland Style Effect Cel Shader",
                "instancePrompt": "borderland style",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-01-07T03:53:05.932",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": True,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "b3b26e38-d8a9-404d-b910-a555e48ec64a", "username": "gruB", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "Borderland Style futuristic fortress shaped like a church, unreal engine, cinematic, 8k",
                        "generated_images": [
                            {
                                "id": "9c59a9e2-a898-4a84-8027-f5df908b5ef3",
                                "url": "https://cdn.leonardo.ai/users/b3b26e38-d8a9-404d-b910-a555e48ec64a/generations/f234eecf-6ca8-4400-813e-c101d33998c5/Borderland_Style_Borderland_Style_futuristic_fortress_shaped_like_a_church_un_0.png",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
        ]
    }
}

custom_models = {
    "data": {
        "custom_models": [
            {
                "id": "444cd35a-55c7-4e49-83ad-8660d993edc3",
                "name": "the Drya",
                "description": "",
                "instancePrompt": "the Drya",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-04T19:26:51.187",
                "sdVersion": "v1_5",
                "type": "CHARACTERS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "7ab2c0de-12ed-4e10-941d-220575b14375", "username": "zserv", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/7ab2c0de-12ed-4e10-941d-220575b14375/generations/33ca9e68-d19a-4d35-910b-8d6b3c52bb15/the_Drya_the_Drya_as_toon_female_character_perfect_single_face_an_2.jpg",
                    "id": "efe26642-7d71-43d4-915b-243e80432cf2",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "(( the Pauk ) as an Nefertity )  | Horror Theme Steampunk | (single head) | Frontal view | centered | perfect anatomy | key visual | intricate | highly detailed | breathtaking | precise lineart | vibrant | abstract | Lovecraftian Noir | cinematic | Carne Griffiths | Conrad Roset hyper-perfect in-depth details, mind-blowing natural vivid colors, ultra-sharp, upscaled 8x, fine lines, cinematic lights, ultra wide scene, high in-depth details, Hollywood quality, a masterpiece, ultra high detailed designs, Camera: Sony A1 200MP, Lens: 85mm f/1.4, Shutter speed: 1/12 ISO:40, 24K, RAW, Sharpness from 1 to 100 (0), Noise from 1 to 100 (0), Post-processing in Adobe Lightroom, photorealistic , ultra photoreal , ultra detailed, intricate details",
                        "generated_images": [
                            {
                                "id": "516ac2b2-cdac-47cf-9cad-12504c7bd759",
                                "url": "https://cdn.leonardo.ai/users/f1410d36-7283-4575-8a2b-a4b8d806285c/generations/aa32b2a3-b278-4611-b175-28a69ee4a1ef/the_Drya_the_Pauk_as_an_Nefertity_Horror_Theme_Steampunk_single_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "f84690eb-cfe7-431c-afd4-ccc2d628bede",
                "name": "T Borodinauskas",
                "description": "",
                "instancePrompt": "T Borodinauskas",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-04T19:21:09.279",
                "sdVersion": "v1_5",
                "type": "CHARACTERS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "7ab2c0de-12ed-4e10-941d-220575b14375", "username": "zserv", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/7ab2c0de-12ed-4e10-941d-220575b14375/generations/b87ae51b-ed39-45a5-8f87-0d80e0c56107/T_Borodinauskas_T_Borodinauskas_as_roaring_single_faced_single_perfect_wid_0.jpg",
                    "id": "6fed79b1-6a86-40c8-a360-4a22ba8ab580",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "Full body of Colorful T Borodinauskas: black and red ink flow: 8k resolution photorealistic masterpiece: by Aaron Horkey and Jeremy Mann, detailed gorgeous face and eyes, fine detailed face, intricately detailed fluid gouache painting: by Jean Baptiste Mongue: calligraphy: acrylic: watercolor art, professional photography, natural lighting, volumetric lighting maximalist photoillustration: by marton bobzert: 8k resolution concept art intricately detailed, complex, elegant, expansive, fantastical",
                        "generated_images": [
                            {
                                "id": "7d7a6879-9f6b-4e11-b0ca-99e4c43c39c5",
                                "url": "https://cdn.leonardo.ai/users/7ab2c0de-12ed-4e10-941d-220575b14375/generations/8f0f866d-9fa1-447a-812e-c56b782a670f/T_Borodinauskas_Full_body_of_Colorful_T_Borodinauskas_black_and_red_ink_flow_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "26aab27c-fd9d-4238-b6d4-dd193f3edee2",
                "name": "D O O M S A Y E R",
                "description": "Generates occult priest, dark druids, and worshippers of doom (with a post-apocalyptic spin).",
                "instancePrompt": "A doomsayer",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-04T17:53:33.228",
                "sdVersion": "v1_5",
                "type": "CHARACTERS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "4504b091-46ed-4471-ad0d-5a650533c743",
                    "username": "garbageguy420",
                    "__typename": "users",
                },
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "A doomsayer",
                        "generated_images": [
                            {
                                "id": "21e7f193-6c00-46e2-bf55-d796ddc34f28",
                                "url": "https://cdn.leonardo.ai/users/4504b091-46ed-4471-ad0d-5a650533c743/generations/54606343-89f9-4183-be9c-3eb48d059362/D_O_O_M_S_A_Y_E_R_A_doomsayer_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "611c7c61-bacf-4909-8de8-e2c5cde907a7",
                "name": "Anime Girls 1.0",
                "description": "Anime girls",
                "instancePrompt": "anime style",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-04T17:01:22.834",
                "sdVersion": "v1_5",
                "type": "CHARACTERS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "ce602c4c-6467-4373-b6c8-7516eb20fb87", "username": "Kryt", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "beautiful lady, freckles, dark makeup, hyperdetailed photography, soft light, head and shoulders portrait, cover",
                        "generated_images": [
                            {
                                "id": "554594af-3394-495e-a936-43b61340b124",
                                "url": "https://cdn.leonardo.ai/users/ce602c4c-6467-4373-b6c8-7516eb20fb87/generations/d3199936-b13e-4a96-8137-fa8c8215dab2/Anime_Style_10_beautiful_lady_freckles_dark_makeup_hyperdetailed_photograp_1.jpg",
                                "likeCount": 12,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "12e494cf-1ed0-4b08-b2a1-c7b5b6221c0f",
                "name": "Razumov Portrait Style",
                "description": "Portraits in the style of K. razumov",
                "instancePrompt": "A portrait of",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-04T16:53:29.778",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "daf80667-2bb3-4975-83c0-5115d5c0b85e", "username": "RickH1950", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/daf80667-2bb3-4975-83c0-5115d5c0b85e/generations/5c40f7af-179e-4534-96b5-92b53d5500ae/Razumov_Portrait_Style_a_photorealistic_portrait_of_stunningly_0.jpg",
                    "id": "03bf6882-abef-4ea2-9996-444bf26e8e67",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a beautiful girl, freckles, dark makeup,  flat color, wide angle, clean detailed faces, intricate clothing, analogous colors, glowing shadows, beautiful gradient, depth of field, clean image, high quality, high detail, high definition, soft light",
                        "generated_images": [
                            {
                                "id": "a2b7cf74-64b2-486b-b2f2-98b0c6a3401f",
                                "url": "https://cdn.leonardo.ai/users/5155974e-5b3a-4872-b613-3e3ea57b055b/generations/c27b559b-8059-43d9-9ed1-6f0d99dd5110/Razumov_Portrait_Style_a_beautiful_girl_freckles_dark_makeup_flat_color_wide_angl_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "d96b9c5d-89db-48b9-bbb7-2f3b5c74dbdc",
                "name": "Summer frozen sweets",
                "description": "water color on white background cartoon type images of frozen sweets",
                "instancePrompt": "an ice cream cone",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-04T16:28:59.16",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "a4735e05-b1fb-4af6-aa04-af9d40c7d438", "username": "boop749", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "watercolor clipart for sticker summer ice cream cone",
                        "generated_images": [
                            {
                                "id": "b9eda412-8b6c-4d41-8eb8-7bdfc0d8cca8",
                                "url": "https://cdn.leonardo.ai/users/a4735e05-b1fb-4af6-aa04-af9d40c7d438/generations/909f0b73-5a49-4726-88c7-0f1ba0034d07/Summer_frozen_sweets_watercolor_clipart_for_sticker_summer_ice_cream_cone_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "4ed57cd2-9e06-496d-abbe-b7e01f9a09e2",
                "name": "Crypto Dreams",
                "description": "Crypto NFT art based on BAYC",
                "instancePrompt": "An NFT character",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-04T15:42:05.752",
                "sdVersion": "v2",
                "type": "ILLUSTRATIONS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "7bb48ccd-354a-4f0b-8aff-a8eebe8ee8d8", "username": "ElChuba", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/7bb48ccd-354a-4f0b-8aff-a8eebe8ee8d8/generations/77cb48c0-2e8b-4004-9bb1-54a249f0ee6f/Crypto_Dreams_an_zebra_as_an_nft_character_1.jpg",
                    "id": "80e0a3c5-5af0-4b42-8c10-7a1c0a5dd952",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "bayc, a bored ape by All Seing Seneca",
                        "generated_images": [
                            {
                                "id": "817d9122-6f14-41b1-8156-2fbf23cd99ed",
                                "url": "https://cdn.leonardo.ai/users/7bb48ccd-354a-4f0b-8aff-a8eebe8ee8d8/generations/2d7e4972-8033-4e87-8651-abf658215ae5/Crypto_Dreams_bayc_a_bored_ape_by_All_Seing_Seneca_1.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "f70cb462-f48e-4c48-bf15-948a9718938a",
                "name": "e-commerce landing page",
                "description": "",
                "instancePrompt": "landing page electronics ",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-04T14:19:23.18",
                "sdVersion": "v2",
                "type": "UI_ELEMENTS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "2e4d5a04-f8cd-41a1-b082-072d56b1fbeb", "username": "Viniciusm", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "landing page,",
                        "generated_images": [
                            {
                                "id": "054d4120-a1fe-4432-8cb5-15b81a073057",
                                "url": "https://cdn.leonardo.ai/users/2e4d5a04-f8cd-41a1-b082-072d56b1fbeb/generations/d8bf9617-14db-4849-8852-2f5e1d46d822/landing_landing_page_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "b4fa336a-8b38-4a7e-a709-7670a89f1bd0",
                "name": "flag",
                "description": "flag",
                "instancePrompt": "flag",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-04T13:52:27.78",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "cc3f8064-77f7-4809-8be4-feba69b5b80b",
                    "username": "SlimeHammer",
                    "__typename": "users",
                },
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "flag of frog",
                        "generated_images": [
                            {
                                "id": "c5d5100f-c264-4c3b-bdd2-92148dd16b19",
                                "url": "https://cdn.leonardo.ai/users/cc3f8064-77f7-4809-8be4-feba69b5b80b/generations/101643e0-9eb0-454e-871c-8498874acac0/flag_flag_of_frog_1.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "65ddee39-562f-4005-8376-015a618f8f70",
                "name": "liliana15",
                "description": "",
                "instancePrompt": "a portrait of liliana15",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-04T13:36:34.166",
                "sdVersion": "v1_5",
                "type": "CHARACTERS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "4b788d63-9078-4dc8-9da4-6dcae596f0f3",
                    "username": "awesomeuser",
                    "__typename": "users",
                },
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a portrait of liliana15, levitation, hovering, full body, 1 character, 1 body, centered character",
                        "generated_images": [
                            {
                                "id": "af063ec8-ecf9-4d87-85d8-d10792a6b6ad",
                                "url": "https://cdn.leonardo.ai/users/4b788d63-9078-4dc8-9da4-6dcae596f0f3/generations/9f73bf2e-af36-4c1c-9fb5-6d1fb2336ddb/liliana15_a_portrait_of_liliana15_levitation_hovering_full_body_1_chara_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "37001f04-f71f-44b3-b40d-cb0ecef690c1",
                "name": "Mamulena",
                "description": "Beautiful woman with brown eyes",
                "instancePrompt": "beautiful woman with brown eyes, beautiful woma",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-04T11:26:53.606",
                "sdVersion": "v1_5",
                "type": "PHOTOGRAPHY",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "ec4c8a0a-bae6-4f33-b62c-ec6fa756fc47",
                    "username": "Securbond_Phone",
                    "__typename": "users",
                },
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/ec4c8a0a-bae6-4f33-b62c-ec6fa756fc47/generations/deaae567-e251-4e45-b809-777cd87e9dd3/Mamulena_crown_of_roses_on_the_head_earrings_necklaces_35mm_284185531_0.jpg",
                    "id": "5d7019bd-ca1e-43ee-b663-947c899f7ce1",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "Gorgeous brunette, beautiful woman, wavy hair falls on her shoulders, playful look, dressed in an intricately designed light detailed black dress, extremely attractive, flirtatious and playful, neon glow, cloudy fantasy, excellent proportions of the female body, futuristic landscape, bright view, beautiful clearly defined armpits, fantasy adventure theme, extremely attractive, perfect slender female anatomy, film photography, analog photography, film grain, extreme detail, 4k, ultra HD, anna dittmann, hyperrealism, trending on artstation, polished, beautiful, shining, synesthesia, bright, photorealistic, backlight, hair light, 8k resolution, unreal engine 5",
                        "generated_images": [
                            {
                                "id": "406272d8-9ebc-4d85-8c1b-258ab9987516",
                                "url": "https://cdn.leonardo.ai/users/720bd193-a7ea-4181-add2-68cb32b5ee6d/generations/59fc26aa-727f-4af8-81db-290b09d48a3a/Mamulena_Gorgeous_brunette_beautiful_woman_wavy_hair_falls_on_her_shou_1.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "dc8b1dc6-30a0-418f-b5db-a8deadc9d5e5",
                "name": "Character portrait",
                "description": "Good for creating fantasy portrait of human face. Best to use at 640x832. Keep promp weight at 7-9. Remember to add (a portrait of ) at the beginning of your prompt for best results.",
                "instancePrompt": "Face",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-04T10:48:18.382",
                "sdVersion": "v1_5",
                "type": "CHARACTERS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "c5e92e90-48cb-4fa1-ae9f-f2b0530e6adf", "username": "Valsiren", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/c5e92e90-48cb-4fa1-ae9f-f2b0530e6adf/generations/82d01f47-41f2-495d-81e0-08bf2c7396f9/Random_face_34_shot_full_body_image_of_Insanely_detailed_photograph_of_A_0.jpg",
                    "id": "f189138f-a971-4887-919e-1caf30cab7ea",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "3/4 shot full body image of Insanely detailed photograph of An elaborate beautiful temptress glossy lipstick intricate glistening skin face long hair hyperdetailed painting, emerging out of waterfall, Tom Bagshaw Dan Witz CGSociety ZBrush Anna dittmann Central fantasy art 4K",
                        "generated_images": [
                            {
                                "id": "f189138f-a971-4887-919e-1caf30cab7ea",
                                "url": "https://cdn.leonardo.ai/users/c5e92e90-48cb-4fa1-ae9f-f2b0530e6adf/generations/82d01f47-41f2-495d-81e0-08bf2c7396f9/Random_face_34_shot_full_body_image_of_Insanely_detailed_photograph_of_A_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "f1830509-5b3e-48d5-a57d-923815ca7a0c",
                "name": "Little Heroes",
                "description": "Make a Little Heroes",
                "instancePrompt": "Little Wonder Women",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-04T07:46:12.362",
                "sdVersion": "v1_5",
                "type": "CHARACTERS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "463c9248-5fbd-4be6-91c5-a5e6e4ef9240", "username": "Remix", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/463c9248-5fbd-4be6-91c5-a5e6e4ef9240/generations/3a71a947-3a2c-4410-9075-12f0fdad630c/Little_Heroes_Little_Superman_white_costume_3d_full_body_highly_detailed_v_2.jpg",
                    "id": "aa1a7e33-629a-48ea-9310-c9ba6921c586",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "Little Wonder Women",
                        "generated_images": [
                            {
                                "id": "5b2cf668-1b5f-4e4a-ae1a-14dc4dd43166",
                                "url": "https://cdn.leonardo.ai/users/463c9248-5fbd-4be6-91c5-a5e6e4ef9240/generations/e02a7c58-b7e4-42db-8422-0dcdd28a3de1/Little_Heroes_Little_Wonder_Women_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "b260b08d-9db0-442c-b1d3-2604ccd330a7",
                "name": "Cookie Run-v1",
                "description": "",
                "instancePrompt": "cookie run",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-04T06:25:36.973",
                "sdVersion": "v1_5",
                "type": "ILLUSTRATIONS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "2f0e87f7-44f6-4081-baeb-c7ea3023703a", "username": "Andrek", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/2f0e87f7-44f6-4081-baeb-c7ea3023703a/generations/c0403e67-5be9-488c-b681-a75a83ffb5a5/Cookie_Runv1_A_cookie_run_character_who_doesnt_exist_in_the_game_yet_but_0.jpg",
                    "id": "739b695d-61fe-4a37-b11e-e0973d534cd9",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": " A whimsical cookie run character with a mischievous smile, wearing a colorful striped shirt and a baker's hat.",
                        "generated_images": [
                            {
                                "id": "49993490-2edc-4942-8175-2b990915c5c0",
                                "url": "https://cdn.leonardo.ai/users/2f0e87f7-44f6-4081-baeb-c7ea3023703a/generations/bde10e1f-a6fc-4cd2-aed8-f8424bb4545d/Cookie_Runv1_A_whimsical_cookie_run_character_with_a_mischievous_smile_w_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "5d77afd8-8f15-48fe-bb8e-30d62f9ff8fa",
                "name": "Coldplay",
                "description": "Model for IA to recognize the Coldplay Band Members",
                "instancePrompt": "Chris Martin from Coldplay",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-04T05:37:37.855",
                "sdVersion": "v1_5",
                "type": "CHARACTERS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "419d1a7b-9f0a-45c3-a7f1-617a535a9c96",
                    "username": "imanolSante18",
                    "__typename": "users",
                },
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "Chris Martin from Coldplay, marvel comics, avengers, iron man suit, full body render, rembrandt, cgsociety, artstation trending, highly detailed, ultra realistic, concept art, intricate details, eerie, highly detailed, photorealistic, octane render, 8 k, unreal engine.",
                        "generated_images": [
                            {
                                "id": "8842a983-fc27-473e-a443-2bf4e3caf166",
                                "url": "https://cdn.leonardo.ai/users/419d1a7b-9f0a-45c3-a7f1-617a535a9c96/generations/eca231af-25ee-4300-b740-9de1fa9c0aff/Coldplay_Chris_Martin_from_Coldplay_marvel_comics_avengers_iron_man_su_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "3474e4c5-11cc-419a-be7b-72654fd2ac4e",
                "name": "Typography 1",
                "description": "Creates images with words in solid style.",
                "instancePrompt": "word",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-04T05:34:13.553",
                "sdVersion": "v2",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "ca09e017-65ce-4c95-a06e-2390232398bb", "username": "Archie007", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "Logo design, travel, Hotels",
                        "generated_images": [
                            {
                                "id": "ae759317-eaee-474c-9a9c-4f4db29ffa72",
                                "url": "https://cdn.leonardo.ai/users/dfedd259-c3d7-46f9-a36d-fa2a33bf114f/generations/7d2c1903-3ddf-4b74-98e2-823f46f2c6fa/Typography_1_Logo_design_travel_Hotels_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "f232eee3-5be9-467b-a0c8-6c65311040c7",
                "name": "Black and White Portraits",
                "description": "Black and White Portraits",
                "instancePrompt": "Portrait",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-04T05:12:29.909",
                "sdVersion": "v2",
                "type": "PHOTOGRAPHY",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "ee3d46dc-fcd3-4cb4-a7ca-e3d94847f3e5",
                    "username": "ProfTeddington",
                    "__typename": "users",
                },
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "Ginger man with short beard and glasses, portrait",
                        "generated_images": [
                            {
                                "id": "edc5ffc1-22e4-45d7-9da9-2c8f595d34e1",
                                "url": "https://cdn.leonardo.ai/users/ee3d46dc-fcd3-4cb4-a7ca-e3d94847f3e5/generations/514ea837-573c-49b5-a4ec-ff72c633dd86/Black_and_White_Portraits_Ginger_man_with_short_beard_and_glasses_portrait_3.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "ad6f6660-693b-4d29-8d55-07b85d52ad55",
                "name": "LitKillah",
                "description": "LitKillah",
                "instancePrompt": "LitKillah",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-04T04:30:52.253",
                "sdVersion": "v1_5",
                "type": "CHARACTERS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "ade3a833-b65f-4187-ad6e-f28e02666e7e", "username": "NowDesign", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "LitKillah wearing sunglasses, fullbody shot, unreal engine, 3d rendered, extremely detailed, volumetric lighting, 8k, high resolution, polished",
                        "generated_images": [
                            {
                                "id": "92248a6a-02ee-463f-beb9-31d9de90d70b",
                                "url": "https://cdn.leonardo.ai/users/ade3a833-b65f-4187-ad6e-f28e02666e7e/generations/969b5d99-4278-4312-9538-605a0fd751ee/LitKillah_LitKillah_wearing_sunglasses_fullbody_shot_unreal_engine_3d_r_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "34cf15f4-5bcd-4563-a9ce-feecccabf5c9",
                "name": "Tiktoker Generator",
                "description": "Generate a new tiktoker!",
                "instancePrompt": "A tiktoker",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-04T02:10:27.299",
                "sdVersion": "v2",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "9afdb51a-2f05-4911-a4e5-36bf15ac4edf",
                    "username": "myawsomename",
                    "__typename": "users",
                },
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "A tiktoker of a abstract beauty, Lizard Man, centered, looking at the camera, approaching perfection, dynamic, moonlight, highly detailed, watercolor painting, artstation, concept art, smooth, sharp focus, illustration",
                        "generated_images": [
                            {
                                "id": "c2a255cc-077a-4485-8eed-d3edcb796ebf",
                                "url": "https://cdn.leonardo.ai/users/95664c54-3731-4512-8c68-c449364749d3/generations/f7d7547d-1f18-4138-93d5-a7d7a9f28e10/Tiktoker_Generator_A_tiktoker_of_a_abstract_beauty_Lizard_Man_centered_looking_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "8798d8ba-56fa-418d-9d61-9f83d0783087",
                "name": " Custom Mobile Game Items",
                "description": "model to generate images to generate images of magnets in isometric",
                "instancePrompt": "a game item ",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-04T01:24:35.119",
                "sdVersion": "v1_5",
                "type": "GAME_ITEMS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "56547323-5449-448d-8560-27fd38e61b25", "username": "Blademort", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a game item 🏘️",
                        "generated_images": [
                            {
                                "id": "c97a21c0-931c-42a5-b5b2-b85dc3484f33",
                                "url": "https://cdn.leonardo.ai/users/56547323-5449-448d-8560-27fd38e61b25/generations/6d6f5b8b-f271-421f-8367-32543a09b5b4/Custom_Mobile_Game_Items_a_game_item_4.jpg",
                                "likeCount": 1,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "6cb74458-733b-4ef9-96e8-905f9f4d42ba",
                "name": "Pencilistic",
                "description": "A model containing a dataset of pencil drawings on paper, This isn’t near as perfect like traditional artists like how ai isn’t perfect, so expect ...",
                "instancePrompt": "a drawing",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-04T00:58:23.469",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "2f0e87f7-44f6-4081-baeb-c7ea3023703a", "username": "Andrek", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/2f0e87f7-44f6-4081-baeb-c7ea3023703a/generations/29deeeea-1a52-45e4-a847-7eb2500cf65f/Pencilistic_A_drawing_of_a_mug_filled_with_coffee_with_steam_coming_out_G_3.jpg",
                    "id": "ffe8ece4-c02a-449e-b99b-6b937071d832",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "A drawing of a mug filled with coffee, with steam coming out, Graphite, Pencil, Pointillism, Trending on ArtStation",
                        "generated_images": [
                            {
                                "id": "ffe8ece4-c02a-449e-b99b-6b937071d832",
                                "url": "https://cdn.leonardo.ai/users/2f0e87f7-44f6-4081-baeb-c7ea3023703a/generations/29deeeea-1a52-45e4-a847-7eb2500cf65f/Pencilistic_A_drawing_of_a_mug_filled_with_coffee_with_steam_coming_out_G_3.jpg",
                                "likeCount": 2,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "3cbb2148-1083-4b7c-a879-46c083a09154",
                "name": "banheiro com banheira",
                "description": "banheiras de hidromassagem",
                "instancePrompt": "hidro1",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-03T23:59:51.704",
                "sdVersion": "v1_5",
                "type": "BUILDINGS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "2c34b750-fbb0-4535-ac81-e7889c5a1c35", "username": "Carolsouza", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a room, small bathroom interior design ,3D scene, black marble  countertop, white metro tiles, wooden slatted wall, round mirror, black mable shower stall, lighting design, corona render, unreal, interior design magazine photograth",
                        "generated_images": [
                            {
                                "id": "67773ce4-a8c5-463e-a6b8-373dc60db6ba",
                                "url": "https://cdn.leonardo.ai/users/2c34b750-fbb0-4535-ac81-e7889c5a1c35/generations/7e3ec43d-0f28-424a-bed1-1e8b1435e5cf/banheiro_com_banheira_a_room_small_bathroom_interior_design_3D_scene_black_marble_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "5ca77967-9ef1-4709-b18e-b5d4c0449075",
                "name": "Cute Anime Girls 1.0",
                "description": "Create anime-style girls in a smooth, flowing stroke",
                "instancePrompt": "smooth anime style",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-03T23:48:09.972",
                "sdVersion": "v1_5",
                "type": "CHARACTERS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "ab0732f8-4ae5-4bd7-8822-e4f24758e7fb",
                    "username": "genesisivor",
                    "__typename": "users",
                },
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/ab0732f8-4ae5-4bd7-8822-e4f24758e7fb/generations/b340f423-f0fd-4733-9967-0fbe714c26d9/Cute_Anime_Girls_10_smooth_anime_style_white_castle_flying_over_the_clouds_in_5.jpg",
                    "id": "6ecef57b-e216-4595-afbc-4df61a428f6b",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "dog girl, blue hair, nice pose, {{depth of field}}, extremely detailed girl, illustration, solo, sharp focus, light smile, closed mouth, beautiful detailed eyes, yellow eyes, {{{{{looking at viewer}}}}},{{{{{sharp focus}}}}}, {loli}, {{{{{masterpiece illustration}}}}},full body, normal angle,, long hair,",
                        "generated_images": [
                            {
                                "id": "1ec2676e-60a5-42e3-b465-3c1eb08f0930",
                                "url": "https://cdn.leonardo.ai/users/ab0732f8-4ae5-4bd7-8822-e4f24758e7fb/generations/15e748c9-3556-4342-aae8-4b171b41ab15/Cute_Anime_Girls_Gen_10_dog_girl_blue_hair_nice_pose_depth_of_field_extremely_det_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "f19e584a-b678-4015-89d5-833fff66a6e2",
                "name": "Aesthetic friend group pictures",
                "description": "generate some friend goals pictures!",
                "instancePrompt": "Aesthetic friend group",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-03T23:45:44.239",
                "sdVersion": "v2",
                "type": "PHOTOGRAPHY",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "9afdb51a-2f05-4911-a4e5-36bf15ac4edf",
                    "username": "myawsomename",
                    "__typename": "users",
                },
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": " framework ",
                        "generated_images": [
                            {
                                "id": "35119233-0f41-49d1-8c75-6280534913e8",
                                "url": "https://cdn.leonardo.ai/users/7b925e04-af28-4c7e-aad4-1c66cc671ff9/generations/9b9865f9-e8c7-48d6-b2b3-97a208a1d4ac/Aesthetic_friend_group_pictures_framework_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "c52bcbca-30c3-417f-a660-151c34600173",
                "name": "vsco/preppy girls",
                "description": "",
                "instancePrompt": "vsco/preppy girl aesthetic",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-03T23:38:14.908",
                "sdVersion": "v2",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "9afdb51a-2f05-4911-a4e5-36bf15ac4edf",
                    "username": "myawsomename",
                    "__typename": "users",
                },
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "Create an Afrofuturist, surrealist, cyberpunk Igbo Mbari mask with intricate details, featuring colorful ceramic textures depicting asymmetrical faces with exaggerated eyes and whimsical features. The mask should challenge traditional European conceptions of beauty, with a focus on vibrant colors and playful shapes.  To achieve the desired ceramic texture, use simple geometric shapes and patterns to create a tiled effect. Avoid using complex gradients or detailed shading, instead relying on bold, contrasting colors to create depth and texture.  To further convey the surreal and cyberpunk themes of the mask, incorporate elements of futuristic technology and machinery into the design. These can be represented through simple shapes like gears, wires, or circuit boards, and should be used sparingly to avoid overwhelming the design.  Finally, to tie the design back to its cultural roots, incorporate elements of the Igbo Mbari tradition into the mask, such as geometric patterns, stylized ani",
                        "generated_images": [
                            {
                                "id": "f3b302b1-9711-4f39-b178-abc07635f23c",
                                "url": "https://cdn.leonardo.ai/users/6c582e58-fa16-4671-b148-3aab75e95266/generations/6067c115-9be5-46aa-be03-e1c61c2184b1/vscopreppy_girls_Create_an_Afrofuturist_surrealist_cyberpunk_Igbo_Mbari_mask_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "72c19c5d-06fd-42b5-9d01-1a9c80a0cc22",
                "name": "Blythe Fantasy",
                "description": "beautifull Doll",
                "instancePrompt": "DOLL",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-03T23:05:44.022",
                "sdVersion": "v1_5",
                "type": "ILLUSTRATIONS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "d068039c-99eb-4776-9309-4de03c12dea1",
                    "username": "UpsetKitty_",
                    "__typename": "users",
                },
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "lemon man relaxing on chair on beach drinking cocktail with boombox and seagulls and palmtree, photorealistic, hyperdetailed, golden ratio, cartoon, pixar, hdr, octane render, trending on artstation, cinematography lighting, ",
                        "generated_images": [
                            {
                                "id": "66bbb033-3543-4c02-9b0c-d9efcd273f9f",
                                "url": "https://cdn.leonardo.ai/users/5b8c64d4-6a65-4864-b3dd-4668d4a378e2/generations/d3d4b5a3-db6f-4e63-ae76-93677fdbff49/Blythe_Fantasy_lemon_man_relaxing_on_chair_on_beach_drinking_cocktail_with_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "9e6e1a43-86b5-46b9-828a-ec1cef8f616e",
                "name": "Ankhegs",
                "description": "Ankhegs are huge insectoid monster with many slender limbs and large antennae",
                "instancePrompt": "Ankheg",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-03T22:39:49.204",
                "sdVersion": "v1_5",
                "type": "PHOTOGRAPHY",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "d9739cd5-d837-40b9-9f7c-52701bcf837a",
                    "username": "BenTheArtMan",
                    "__typename": "users",
                },
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "A Ankheg, its mandibles dripping with venom, perched atop a pristine white snowdrift.",
                        "generated_images": [
                            {
                                "id": "ed89a763-af79-419f-bd84-37be0c9e4318",
                                "url": "https://cdn.leonardo.ai/users/d9739cd5-d837-40b9-9f7c-52701bcf837a/generations/ab3fae85-a858-4ae0-a75c-6b39380beaa7/Ankhegs_A_Ankheg_its_mandibles_dripping_with_venom_perched_atop_a_pri_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "d984c24a-aa4c-4823-9ef3-b0dde9d21d86",
                "name": "2ds",
                "description": "2D Surreal Fantasy Yoshitaka Amano and aAyumi Kasai style",
                "instancePrompt": "A human being",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-03T22:32:56.93",
                "sdVersion": "v2",
                "type": "ILLUSTRATIONS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "2f511681-fe38-4be5-8e24-1d820c3103f4",
                    "username": "paulangelogc",
                    "__typename": "users",
                },
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "A 2d surreal illustration of  a RPG Character in the path of self love and autorecognition, high quality, hand made, and yoshitaka amano style",
                        "generated_images": [
                            {
                                "id": "b9c7fe7b-2794-40f2-a1ee-2ab6fb93927a",
                                "url": "https://cdn.leonardo.ai/users/2f511681-fe38-4be5-8e24-1d820c3103f4/generations/2df20f6a-0143-4fed-9e4d-e2cb166e8925/2ds_A_2d_surreal_illustration_of_a_RPG_Character_in_the_path_of_2.jpg",
                                "likeCount": 2,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "e86fa62a-7b1e-472b-9416-12be31a8bc8d",
                "name": "Supergirls",
                "description": "compilation of comic style art of female characters only",
                "instancePrompt": "Sgirls",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-03T22:14:45.492",
                "sdVersion": "v1_5",
                "type": "ILLUSTRATIONS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "cd5af38f-3279-4af2-bc9d-a2b267fee0f7",
                    "username": "Soyisraruiz",
                    "__typename": "users",
                },
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/cd5af38f-3279-4af2-bc9d-a2b267fee0f7/generations/575c57e9-2007-46ab-a1f4-92df2120d676/Supergirls_girl_dressed_in_leather_jacket_with_the_zipper_of_the_jacket_0.jpg",
                    "id": "455d4e01-3567-4562-a5c7-4e9606780681",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "girl dressed in leather jacket, with the zipper of the jacket open without clothes inside, pink jean pants, dark glasses, hiding both hands behind her back, girl with straight hair, face with Asian features.",
                        "generated_images": [
                            {
                                "id": "c4893da8-633b-49b0-8df5-356b5f9dcf1f",
                                "url": "https://cdn.leonardo.ai/users/cd5af38f-3279-4af2-bc9d-a2b267fee0f7/generations/dfe5513b-1d7c-4ba3-bdb4-0abd6fa0d35b/Supergirls_girl_dressed_in_leather_jacket_with_the_zipper_of_the_jacket_0.jpg",
                                "likeCount": 4,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "db524da0-4a30-4516-8f6b-b15e58ebd1ab",
                "name": "The Prince's Lost Toys",
                "description": " colorful light, intricate, highly detailed, my rendition, artstation, illustration, art by alphonse mucha and uang guangjian and gil elvgren and s...",
                "instancePrompt": "anime prince",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-03T22:11:24.804",
                "sdVersion": "v2",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "08fa806b-b4a5-424a-9efc-efd5978e1e61", "username": "DAigotenno", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "(portrait of disney anime 6 year old prince)surrounded by gold and silver magical toys, colorful light, intricate, elegant, highly detailed, my rendition, artstation, illustration, art by alphonse mucha and uang guangjian and gil elvgren and sachin teng, (symmetry) , octane render, ultra realistic, intricate, digital art, ambient lighting, highly detailed, unreal engine, digital painting, concept art, sharp focus ",
                        "generated_images": [
                            {
                                "id": "9385738b-9596-4ab8-ae3b-e7262514d94c",
                                "url": "https://cdn.leonardo.ai/users/08fa806b-b4a5-424a-9efc-efd5978e1e61/generations/cd674fb9-9f2c-457c-872e-10e9a41b896a/The_Princes_Lost_Toys_portrait_of_disney_anime_6_year_old_princesurrounded_by_go_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "e9734aa0-00f5-4488-b76a-31cc60195023",
                "name": "kpop idol generator",
                "description": "",
                "instancePrompt": "A kpop idol",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-03T22:04:21.041",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "9afdb51a-2f05-4911-a4e5-36bf15ac4edf",
                    "username": "myawsomename",
                    "__typename": "users",
                },
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "A kpop idol",
                        "generated_images": [
                            {
                                "id": "4128f051-b707-4833-a871-1bb5da5c8b50",
                                "url": "https://cdn.leonardo.ai/users/9afdb51a-2f05-4911-a4e5-36bf15ac4edf/generations/14514b9f-4475-4e4b-8c59-54ec46a7f077/kpop_idol_generator_A_kpop_idol_3.jpg",
                                "likeCount": 1,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "2f6ed8eb-8c40-4bb2-97bc-fbc1aab88d95",
                "name": "Pixar/Disney",
                "description": "Pixar/Disney",
                "instancePrompt": "ObiPD",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-03T21:51:30.584",
                "sdVersion": "v1_5",
                "type": "CHARACTERS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "0c3ebcdc-889c-4f2a-980e-68ba77c7b843", "username": "Obiconcept", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/0c3ebcdc-889c-4f2a-980e-68ba77c7b843/generations/a83cd3d0-3063-445f-96f4-cd321c35ebb0/PixarDisney_cute_character_ultra_detailed_perfect_scenery_mysterious_prod_1.jpg",
                    "id": "368bd51d-250e-450e-8d2c-064a38d8d0c0",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "cute character, ultra detailed, perfect scenery, mysterious, glow, product photography, octane render, 8K ultra detailed, perfect scenery, mysterious, glowing green, product photography, octane render, 8K",
                        "generated_images": [
                            {
                                "id": "c36a5865-16c2-46e1-af58-59a953ff753d",
                                "url": "https://cdn.leonardo.ai/users/0c3ebcdc-889c-4f2a-980e-68ba77c7b843/generations/31426272-22ac-4ec9-bdf7-2602e2c9dfda/PixarDisney_cute_character_ultra_detailed_perfect_scenery_mysterious_glow_0.jpg",
                                "likeCount": 6,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "9b52bcfb-de0f-40ab-b8fc-c39d8229fb69",
                "name": "Ice Sculptures",
                "description": "model to generate images of ice sculptures",
                "instancePrompt": "a ice sculpture ",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-03T21:21:13.52",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "56547323-5449-448d-8560-27fd38e61b25", "username": "Blademort", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/56547323-5449-448d-8560-27fd38e61b25/generations/4fa07504-8215-4985-be5d-dd6d1eb5bc5a/Ice_Sculptures_a_ice_sculpture_tree_4.jpg",
                    "id": "2f5da5b2-0278-406e-bee4-5b4d638e01d8",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a ice sculpture 🤖",
                        "generated_images": [
                            {
                                "id": "7d12f018-f8e3-4bd4-94a0-f646bf8bb647",
                                "url": "https://cdn.leonardo.ai/users/56547323-5449-448d-8560-27fd38e61b25/generations/382a80ea-e8b7-4ec0-9b16-183078256baf/Ice_Sculptures_a_ice_sculpture_4.jpg",
                                "likeCount": 5,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "dac0968c-65b5-4d4c-8d9a-83084fa3762b",
                "name": "Game maps v1.8",
                "description": "model to generate images of game maps",
                "instancePrompt": "a game map",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-03T21:15:41.96",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "56547323-5449-448d-8560-27fd38e61b25", "username": "Blademort", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a game map",
                        "generated_images": [
                            {
                                "id": "315b6fa2-9031-40eb-949f-6f13afd8d7b9",
                                "url": "https://cdn.leonardo.ai/users/56547323-5449-448d-8560-27fd38e61b25/generations/abc1226a-4801-4a1c-afc9-93fba686c33b/Game_maps_v18_a_game_map_0.jpg",
                                "likeCount": 4,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "577cc4ff-72ba-44e4-baf3-88bb7031d780",
                "name": "Movie/Tv show  Poster generator",
                "description": "",
                "instancePrompt": "Movie poster",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-03T20:45:56.585",
                "sdVersion": "v2",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "a55cb11c-af6b-40fa-8ef9-0910c3c139f2",
                    "username": "toriropedhis",
                    "__typename": "users",
                },
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": " The Twilight Zone, 8k resolution concept art intricately detailed, complex, elegant, expansive, fantastical, Masterpiece, best quality, chiaroscuro lighting, sfumato texture-collodion process  fractal recursion chaos, plasma fireball of verdigris in the distance, octane render, chromatic density, chromatography ,background=fractal recursion chaos",
                        "generated_images": [
                            {
                                "id": "8c77d196-2e2b-4deb-acbc-9fc2652fc98f",
                                "url": "https://cdn.leonardo.ai/users/ca86fddb-0c8a-45c8-9adc-51e25b5aef3a/generations/f5ca5b37-e313-4a8c-9f98-3ba3e3ae37ac/MovieTv_show_Poster_generator_The_Twilight_Zone_8k_resolution_concept_art_intricately_d_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "0dec12b4-0719-46ca-a15a-3faeb975d4bf",
                "name": "Hokuto no ken character generator",
                "description": "Create a character with Kenshiro School Hokuto",
                "instancePrompt": "warrior, martial fighter",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-03T20:34:10.941",
                "sdVersion": "v1_5",
                "type": "CHARACTERS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "81cdba52-88eb-4760-a5ae-879af1da7808", "username": "huangugu", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/81cdba52-88eb-4760-a5ae-879af1da7808/generations/68f6945e-826d-43bf-af8f-b4c0a9d0c7b8/Hokuto_no_ken_character_generator_a_complete_image_of_a_ninja_in_the_style_Nanto_Seiken_bla_0.jpg",
                    "id": "0605f023-cca9-451d-8795-51c7c05f5100",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a complete image of a fighter in the style hokuto no ken, eyes with details, nose with details, mouth with details, kenshiro, manga style, 8k, octane render, global illumination, very detailed image very well colored, background in white",
                        "generated_images": [
                            {
                                "id": "c97bad23-d174-435d-b6fd-c56ed0fbf598",
                                "url": "https://cdn.leonardo.ai/users/81cdba52-88eb-4760-a5ae-879af1da7808/generations/ed04276f-e481-4226-a4be-5004c5f36c8e/Hokuto_no_ken_character_generator_a_complete_image_of_a_fighter_in_the_style_hokuto_no_ken_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "790f5edb-1043-43d5-9dd5-056cc0c65113",
                "name": "Ink / Line Art",
                "description": "BW Ink and Line Art",
                "instancePrompt": "Ink / Line Art",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-03T18:29:15.907",
                "sdVersion": "v2",
                "type": "ILLUSTRATIONS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "0eea719d-525b-40e3-b338-989c7bb0ee2c", "username": "LUKALAB", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/0eea719d-525b-40e3-b338-989c7bb0ee2c/generations/feeb07ac-a2c2-4a5a-a86a-34bbc50107cf/Ink_Line_Art_city_ink_line_art_1.jpg",
                    "id": "d40976a2-3863-4333-a438-0760d3c60b08",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "leaves flying in the air",
                        "generated_images": [
                            {
                                "id": "0e396b06-a901-4766-8d05-f00782855bae",
                                "url": "https://cdn.leonardo.ai/users/0eea719d-525b-40e3-b338-989c7bb0ee2c/generations/cbf7adbc-e893-4984-9f08-e8b74a3b58f0/Ink_Line_Art_leaves_flying_in_the_air_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "02919502-26c4-40d0-b099-445b492bac65",
                "name": "Obey Babay",
                "description": "",
                "instancePrompt": "Obey Babay",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-03T16:11:17.294",
                "sdVersion": "v1_5",
                "type": "CHARACTERS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "e5797a3f-0a7e-46f0-9483-68bab269fc1e", "username": "lapulkin", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/e5797a3f-0a7e-46f0-9483-68bab269fc1e/generations/67fed63c-863c-41fd-a182-7773b4a818f5/Obey_Babay_exact_true_copy_of_Obey_Babay_as_yawning_single_faced_an_2.jpg",
                    "id": "04da61c8-d949-4e82-b639-72bdc77abf4e",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "( exact true copy of ( Obey Babay ) as ape idol)  | Horror Theme Clockpunk | ((single head)) full body illustration | Top view | centered | ((perfect anatomy)) | key visual | intricate | highly detailed | breathtaking | precise lineart | vibrant | abstract | Lovecraftian Noir | cinematic | H.R. Giger | Conrad Roset, diffuse lighting, hyper-perfect in-depth details, mind-blowing natural vivid colors, ultra-sharp, upscaled 8x, fine lines, cinematic lights, ultra wide scene, high in-depth details, Hollywood quality, a masterpiece, ultra high detailed designs, Camera: Sony A1 200MP, Lens: 85mm f/1.4, Shutter speed: 1/12 ISO:40, 24K, RAW, Sharpness from 1 to 100 (0), Noise from 1 to 100 (0), Post-processing in Adobe Lightroom, photorealistic, ultra photoreal, ultra detailed, intricate details",
                        "generated_images": [
                            {
                                "id": "cb15510b-4528-4b05-88ee-cd29d6d646dd",
                                "url": "https://cdn.leonardo.ai/users/e5797a3f-0a7e-46f0-9483-68bab269fc1e/generations/5285376d-6b4a-431e-ba0b-97a59ce2fbc5/Obey_Babay_exact_true_copy_of_Obey_Babay_as_ape_idol_Horror_Theme_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "bab7bc01-7923-4dd4-b766-98f065240ce4",
                "name": "Gangster Paradise",
                "description": "a world and mood of gangsters of 1920",
                "instancePrompt": "Gangster Paradise",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-03T13:44:39.705",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "698e8c2d-f790-4f6b-9c13-c65fa7920deb", "username": "Lugeer", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/698e8c2d-f790-4f6b-9c13-c65fa7920deb/generations/e1c9f06e-c47b-41d1-855e-25636c3fd617/Gangster_Paradise_Gangster_paradise_portrait_of_mafia_inside_a_bar_epic_contra_2.jpg",
                    "id": "91cb46e4-f0f3-4265-936d-2be2d8679ec9",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "Gangster paradise portrait of mafia inside a bar epic contrasted light",
                        "generated_images": [
                            {
                                "id": "477544dc-91c4-4c9c-828f-906a116d5f46",
                                "url": "https://cdn.leonardo.ai/users/698e8c2d-f790-4f6b-9c13-c65fa7920deb/generations/f1cbaf4e-64bb-45b7-98ab-bb2c474d8004/Gangster_Paradise_Gangster_paradise_portrait_of_mafia_inside_a_bar_epic_contra_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "26cb167b-629d-438e-8efc-2eb05d6181f9",
                "name": "Zombie anime ",
                "description": "mushrooms fantasy ",
                "instancePrompt": "Portrait ",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-03T10:19:52.011",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "f4e66010-69af-4262-bb23-827e24c82516", "username": "JonRT", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/f4e66010-69af-4262-bb23-827e24c82516/generations/9f43a7f7-1b82-4c53-8523-4f452496728b/Mixed_modern_european_ink_painting_anime_female_zombie_bobblehead_m_3.jpg",
                    "id": "154d76c7-772c-4b42-a11c-aff921b285ea",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "cartoon rotoscoping robotic cyborg splash art glitch art action painting photography portrait image FLCL anime fashion wearing vintage robot helmet figurine TikTok island boy Kandinsky headdress flat dreads origami woodcut engraving Modern art marble statue Renaissance Delirium tremens Dali & Picasso style depiction of a beautiful animatronic fiber optics embossed multi purpose transfer LED runners Aeon Flux Bosch MC Escher cybertronic city market landscape made of mechanical Mark Ryden surrealism architecture with plasma face paint cyborg tech gears industrial circuitry parts dramatic light sharp focus artstyle Gensho Yasuda by Fausto de martini Wadim Kashin Z.W. gu Jamie Hewlett Antoni Tudisco Frederic Duquette Mumford hideyuki morioka ito ogure vofan victo ngai composition direction Keyshot Chromatic Aberration Global illumination Subsurface scattering Unreal Engine 5 Octane Render Ambient Occlusion Opulent Beautiful imaginative masterpiece 3d liquid detailing fluid acrylic",
                        "generated_images": [
                            {
                                "id": "f9c50f01-ec4c-46bd-8a64-b3a857d0e516",
                                "url": "https://cdn.leonardo.ai/users/f4e66010-69af-4262-bb23-827e24c82516/generations/4350b99f-e9cd-4f72-9426-14f0556f1237/Mixed_cartoon_rotoscoping_robotic_cyborg_splash_art_glitch_art_acti_3.jpg",
                                "likeCount": 2,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "8c4874c0-ec04-4a89-9433-dbf156d914f0",
                "name": "Smoothie",
                "description": "FruTech",
                "instancePrompt": "a Fruity",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-03T09:56:18.619",
                "sdVersion": "v2",
                "type": "BUILDINGS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "4c4490f4-ee5e-4b62-9bc1-9038afa178b6",
                    "username": "ChadUltraF3",
                    "__typename": "users",
                },
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/4c4490f4-ee5e-4b62-9bc1-9038afa178b6/generations/dd553f4d-c7d5-4923-a967-8c43812a8f03/Smoothie_a_fruity_bitcoin_house_1.jpg",
                    "id": "b5ef114a-f034-4c19-accd-27bfc01a63fa",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a fruity city made of berries",
                        "generated_images": [
                            {
                                "id": "b1350d6e-6f8f-4eb4-be2a-8ae72986d549",
                                "url": "https://cdn.leonardo.ai/users/4c4490f4-ee5e-4b62-9bc1-9038afa178b6/generations/b23eae15-48d6-4222-a991-25ac9cf8e0c4/Smoothie_a_fruity_city_made_of_berries_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "ec0dd7d8-306f-48ce-b264-f681ec2ffbf7",
                "name": "Landscape Wallpapers",
                "description": "Create landscape wallpapers with any size, any resolution. See samples on my profile, search 'wallpaper' at https://app.leonardo.ai/profile/noerman",
                "instancePrompt": "4k",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-03T09:42:39.156",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "dbc5103a-ca87-4323-b0c9-12f740e6e773",
                    "username": "misterprompts",
                    "__typename": "users",
                },
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "Tiangong Chinese style",
                        "generated_images": [
                            {
                                "id": "e2d1a9d0-7e85-4227-9f37-e940afa70da1",
                                "url": "https://cdn.leonardo.ai/users/56729e70-0019-4b57-8b6a-0f2d360722f5/generations/0cf2bf9a-5734-43b9-bb0d-497b4c5ff5b4/Landscape_Wallpapers_Tiangong_Chinese_style_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "68b5e616-1834-43dc-a7c5-a0153a6dbc96",
                "name": "Pixel Art Assets",
                "description": "A Dataset for Pixel Art Images, but not just the Avatar, but Fullbody NPCs. Trained on Classic Video Games.",
                "instancePrompt": "Pixel Character",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-03T09:15:36.661",
                "sdVersion": "v2",
                "type": "PIXEL_ART",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "0bbab906-ba22-47ef-8985-89ec3959e79e", "username": "bornmedia", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "Full body pose of a mage holding a staff, pixel art, Pixel Character",
                        "generated_images": [
                            {
                                "id": "f46b7aad-759f-406d-8649-f200e5f4c715",
                                "url": "https://cdn.leonardo.ai/users/0bbab906-ba22-47ef-8985-89ec3959e79e/generations/62fdafd0-d189-4184-aa0a-3da22a35df78/Pixel_Art_Assets_Full_body_pose_of_a_mage_holding_a_staff_pixel_art_Pixel_Ch_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "fe94035a-4c12-41c3-a618-c475a9547657",
                "name": "Hong Kong Girl, HK",
                "description": "",
                "instancePrompt": "Hong Kong",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-03T07:36:03.158",
                "sdVersion": "v1_5",
                "type": "CHARACTERS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "832669e4-0939-44a7-92a5-1d1289d806a5", "username": "K2023HK", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "   realistic beautiful no clothes orange haired female pianist performing a majestic galactic melody realistic  with details",
                        "generated_images": [
                            {
                                "id": "efb49db7-84ec-42a1-9e3c-b3416cb84c82",
                                "url": "https://cdn.leonardo.ai/users/ca3d54e7-88d1-41f6-bea4-3412b24e952d/generations/48e91a57-8701-488e-aa9e-7b0272aaebdb/Hong_Kong_Girl_HK_realistic_beautiful_no_clothes_orange_haired_female_pia_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "ee1c44df-e65c-4bdf-9573-067454e3e52a",
                "name": "Viktor Safonkin",
                "description": "",
                "instancePrompt": "Viktor Safonkin",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-03T07:34:13.169",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "c5591d60-7ff7-4ba1-bacd-f3f256ef9190",
                    "username": "zaborservice",
                    "__typename": "users",
                },
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "( exact true copy of ( the Pauk ) as an old pharaon )  | Horror Theme Steampunk | single head illustration | Frontal view | centered | perfect anatomy | key visual | intricate | highly detailed | breathtaking | precise lineart | vibrant | abstract | Lovecraftian Noir | cinematic | Viktor Safonkin, Chinese ice carving, diffuse lighting, hyper-perfect in-depth details, mind-blowing natural vivid colors, ultra-sharp, upscaled 8x, fine lines, cinematic lights, ultra wide scene, high in-depth details, Hollywood quality, a masterpiece, ultra high detailed designs, Camera: Sony A1 200MP, Lens: 85mm f/1.4, Shutter speed: 1/12 ISO:40, 24K, RAW, Sharpness from 1 to 100 (0), Noise from 1 to 100 (0), Post-processing in Adobe Lightroom, photorealistic, ultra photoreal, ultra detailed, intricate details",
                        "generated_images": [
                            {
                                "id": "3851a7a9-62d4-4d16-8f95-f0f536e5c195",
                                "url": "https://cdn.leonardo.ai/users/f1410d36-7283-4575-8a2b-a4b8d806285c/generations/6abde543-0fbe-433a-9d13-4e2af8592ad2/Viktor_Safonkin_exact_true_copy_of_the_Pauk_as_an_old_pharaon_Horror_T_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "54695a14-0fc7-4878-8db9-583721c7f4c8",
                "name": "Obese Famous character ",
                "description": "This model will allow you to generate images of famous people in obese form, in a more streamlined and a little more precise way.",
                "instancePrompt": "a Obese  ",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-03T04:47:54.629",
                "sdVersion": "v1_5",
                "type": "CHARACTERS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "56547323-5449-448d-8560-27fd38e61b25", "username": "Blademort", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a Obese catwoman",
                        "generated_images": [
                            {
                                "id": "47323018-1273-4bc4-ab92-03bbb764dff0",
                                "url": "https://cdn.leonardo.ai/users/56547323-5449-448d-8560-27fd38e61b25/generations/58c5bc51-5a4e-4fcd-a2da-08c7fd6ca7cc/Obese_Famous_character_a_Obese_catwoman_2.jpg",
                                "likeCount": 1,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "020aad14-ab93-4781-8938-1d95eed5c35b",
                "name": "Metropolitan Small Apartments",
                "description": "This model will allow you to generate apartment photography images in metropolitan style and with little space in a more streamlined and a little m...",
                "instancePrompt": "a apartments",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-03-03T04:38:34.738",
                "sdVersion": "v1_5",
                "type": "PHOTOGRAPHY",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "56547323-5449-448d-8560-27fd38e61b25", "username": "Blademort", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a apartments under water ",
                        "generated_images": [
                            {
                                "id": "5642733d-3954-42f5-8448-c7157756c52c",
                                "url": "https://cdn.leonardo.ai/users/56547323-5449-448d-8560-27fd38e61b25/generations/c1015fad-a807-425d-97e6-b17f99b44b02/Metropolitan_Small_Apartments_a_apartments_under_water_2.jpg",
                                "likeCount": 2,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "515602ee-14c2-4881-b54b-19b81dcb55c3",
                "name": "meh idk",
                "description": "mix ",
                "instancePrompt": "cybertech",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-03T04:16:34.94",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "f4e66010-69af-4262-bb23-827e24c82516", "username": "JonRT", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/f4e66010-69af-4262-bb23-827e24c82516/generations/e39ab667-3e71-4c07-ba52-4284a702ed91/meh_idk_modern_european_ink_painting_anime_female_zombie_in_a_lush_m_0.jpg",
                    "id": "b4c95a13-827a-4a1c-8adf-5d8882496aa6",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "female hipster techno astronaut fashion model in a vast Dali landscape with Bosch small forest cities with lush kandinsky falling stars action painting by Jamie Hewlett Alberto Mielgo Mark Ryden Yoko d’Holbachie Yosuke Ueno Todd Schorr Amy Sol Jeff Soto DSLR HDR photo ray tracing ultraperfect asymmetrical ratio composition Relative Apparent Size Keyshot MarmosetToolbag 4 3d liquid detailing nvinkpunk, beautiful detailed realistic Neo noir style, Cinematic, neon lights glow in the background. Cinestill 800T film. Lens flare. Helios 44m, dreamwave colors, depth of field, bokeh, modern art marble statue renaissance+bosch+mark ryden surrealism+3/4 portrait high fashion model cyborg ink punk+with melting liquid led lights fiber optic hair+made of hiroaki takahashi art+ultra perfect composition+3d liquid detailing+fluid acrylic+kandinsky art style a vast shooting star filled sky+compositional direction+visual tension+structural net+an opulent cybernetic city background",
                        "generated_images": [
                            {
                                "id": "b95ba0b4-87cf-4d59-b3e0-02115cfeb8ca",
                                "url": "https://cdn.leonardo.ai/users/f4e66010-69af-4262-bb23-827e24c82516/generations/76672ed1-63fa-4662-90d3-465520e08b3d/Ai_drip_tek_female_hipster_techno_astronaut_fashion_model_in_a_vast_Dal_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "c053b5f4-d9d3-4ab9-8850-dce40a3a1d2f",
                "name": "3D-Alike Comics",
                "description": "Create 3D-alike characters or even scenes, perfect for your comic creations, also great for other usage. Please use simple sentence prompts.",
                "instancePrompt": "3d",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-03T04:01:31.651",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {
                    "id": "dbc5103a-ca87-4323-b0c9-12f740e6e773",
                    "username": "misterprompts",
                    "__typename": "users",
                },
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a superhero named ScamBuster ",
                        "generated_images": [
                            {
                                "id": "00296a84-30e4-4ec1-9dc5-e087fced2745",
                                "url": "https://cdn.leonardo.ai/users/7cb4854b-af78-4cfc-9328-d12404a0e6d3/generations/016688ea-2195-435b-9fd3-03f534a62930/3DAlike_Comics_a_superhero_named_ScamBuster_1.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "4eb7a7ea-dc80-45f5-ab58-f836d1c52fe5",
                "name": "South Park",
                "description": "A South Park trained model.",
                "instancePrompt": "a South Park episode",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-03-03T02:33:53.334",
                "sdVersion": "v1_5",
                "type": "ILLUSTRATIONS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "2f0e87f7-44f6-4081-baeb-c7ea3023703a", "username": "Andrek", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/2f0e87f7-44f6-4081-baeb-c7ea3023703a/generations/5e2f185b-d878-421e-8217-c5053e6215ba/South_Park_A_South_Park_episode_High_quality_illustration_3.jpg",
                    "id": "4215d973-dd4e-4b83-8262-aa0f4249718b",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "A South Park character that doesn’t exist but has a unique design.",
                        "generated_images": [
                            {
                                "id": "4b130145-3240-422e-b65c-4d5550818fe3",
                                "url": "https://cdn.leonardo.ai/users/2f0e87f7-44f6-4081-baeb-c7ea3023703a/generations/e2fdb127-4bf9-4c71-8209-bc488e7cb672/South_Park_A_South_Park_character_that_doesnt_exist_but_has_a_unique_de_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
        ]
    }
}

platform_models = {
    "data": {
        "custom_models": [
            {
                "id": "f1929ea3-b169-4c18-a16c-5d58b4292c69",
                "name": "RPG v5",
                "description": "Anashel returns with another great model, specialising in RPG characters of all kinds.",
                "instancePrompt": None,
                "modelHeight": 832,
                "modelWidth": 640,
                "coreModel": "SD",
                "createdAt": "2023-07-28T12:02:43.911",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/ad43331b-c80c-40e5-8462-304aaaef3584/RPG_v5_a_stunning_photograph_of_a_grotesque_alien_creature_wit_1.jpg",
                    "id": "ea3c5232-3c5d-4b64-bd1a-be698576b769",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "A vibrant cinematic photo of a female adventurer in the jungle, octane render, high quality",
                        "generated_images": [
                            {
                                "id": "8b326529-2403-4238-810c-602a798c8c2c",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/95e14374-eaf9-4ac9-9611-855706aadf45/RPG_v5_A_vibrant_cinematic_photo_of_a_female_adventurer_in_the_0.jpg",
                                "likeCount": 6,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "b63f7119-31dc-4540-969b-2a9df997e173",
                "name": "SDXL 0.9",
                "description": "The latest Stable Diffusion model, currently in Beta.",
                "instancePrompt": None,
                "modelHeight": 768,
                "modelWidth": 1024,
                "coreModel": "SD",
                "createdAt": "2023-07-12T14:37:01.33",
                "sdVersion": "SDXL_0_9",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/9ed4ccd8-649c-4a59-a7bb-9f5b704a91b1/SDXL_09_a_beautiful_woman_vivid_striking_colors_cinematic_phot_0.jpg",
                    "id": "4a5b68d4-ef23-4d36-a1d8-b027287da029",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a beautiful woman, vivid striking colors, cinematic photography",
                        "generated_images": [
                            {
                                "id": "6cea9433-3e8c-4614-8a5e-4cbb969e6699",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/9ed4ccd8-649c-4a59-a7bb-9f5b704a91b1/SDXL_09_a_beautiful_woman_vivid_striking_colors_cinematic_phot_1.jpg",
                                "likeCount": 5,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "d69c8273-6b17-4a30-a13e-d6637ae1c644",
                "name": "3D Animation Style",
                "description": "Great at 3D film vibes, capable of complex scenes with rich color. Storyboard time!",
                "instancePrompt": None,
                "modelHeight": 832,
                "modelWidth": 640,
                "coreModel": "SD",
                "createdAt": "2023-07-04T04:16:46.127",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/0e85d140-3ea0-4179-a708-ae95bf9329a3/3D_Animation_Style_a_masterpiece_image_of_an_older_tired_and_b_2.jpg",
                    "id": "ca1b67dc-8e39-49a8-8846-f930fb286ba9",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a masterpiece image of an older tired and battle-worn male detective named jack smith, highly detailed, HDR, cyberpunk, realistic, (photorealistic:1.4), best quality, ultra high res",
                        "generated_images": [
                            {
                                "id": "aa84be9e-4156-4887-afe8-d7b858cbe0de",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/2183b6e1-29f7-4295-bd86-7ed3fa233d5c/PixarTypeB_a_masterpiece_image_of_an_older_tired_and_battlewor_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "ac614f96-1082-45bf-be9d-757f2d31c174",
                "name": "DreamShaper v7",
                "description": "Lykon is back with another update. This model is great at a range of different styles.",
                "instancePrompt": None,
                "modelHeight": 832,
                "modelWidth": 640,
                "coreModel": "SD",
                "createdAt": "2023-07-04T04:16:25.719",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/911623f3-4a89-4db9-b49f-ace5ac086a3d/DreamShaper_v7_A_vibrant_cinematic_photo_of_a_female_adventure_1.jpg",
                    "id": "52550c00-4def-4283-91f4-ccd196a630bf",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "an older tired and battle-worn male detective, highly detailed, HDR, cyberpunk",
                        "generated_images": [
                            {
                                "id": "fb390f8e-e9d6-4ee8-a67c-7cae9a132bab",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/bff69fae-6e4e-48d1-8a8f-6c75799be511/DreamShaper_v7_an_older_tired_and_battleworn_male_detective_hi_1.jpg",
                                "likeCount": 2,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "e316348f-7773-490e-adcd-46757c738eb7",
                "name": "Absolute Reality v1.6",
                "description": "A photorealistic style model from Lykon. Great at all sorts of photorealism.",
                "instancePrompt": None,
                "modelHeight": 832,
                "modelWidth": 640,
                "coreModel": "SD",
                "createdAt": "2023-07-04T04:15:48.815",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/9d7e2dbe-6dff-4bf5-b487-414dee2a10b9/Absolute_Reality_v16_a_stunning_photo_of_a_woman_with_aztech_t_1.jpg",
                    "id": "cf623adb-d7f3-43e6-8431-d2edd5a7a08e",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a photo of a woman with a tribal headress, stunning photography, masterpiece, hdr",
                        "generated_images": [
                            {
                                "id": "cc14e950-ffdb-41ee-85d0-eb9419956a82",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/4836d001-a2df-4a29-a0dd-11786b857f55/Absolute_Reality_v16_a_photo_of_a_woman_with_a_tribal_headress_2.jpg",
                                "likeCount": 2,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "1aa0f478-51be-4efd-94e8-76bfc8f533af",
                "name": "Anime Pastel Dream",
                "description": "Pastel anime styling. Use with PMv3 and the anime preset for incredible range. Model by Lykon.",
                "instancePrompt": None,
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2023-06-13T06:01:06.314",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/8cc624c3-c1ba-40c9-b3cd-21056382728a/AnimePastelDream_fuji_film_candid_portrait_o_a_black_woman_wea_2.jpg",
                    "id": "c5510862-e82b-4705-861c-58658a89fa9c",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "fuji film candid portrait o a black woman wearing sunglasses rocking out on the streets of miami at night, 80s album cover, vaporwave, synthwave, retrowave, cinematic, intense, highly detailed, dark ambient, beautiful, dramatic lighting, hyperrealistic",
                        "generated_images": [
                            {
                                "id": "66c689b4-dfaa-43c3-8f72-b664db7f21e5",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/db468128-7209-4d2d-9c17-6ddcf6e1f792/AnimePastelDream_fuji_film_candid_portrait_o_a_black_woman_wea_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "b7aa9939-abed-4d4e-96c4-140b8c65dd92",
                "name": "DreamShaper v6",
                "description": "A new update to an incredibly versatile model, excels at both people and environments, by Lykon.",
                "instancePrompt": None,
                "modelHeight": 832,
                "modelWidth": 640,
                "coreModel": "SD",
                "createdAt": "2023-05-26T02:29:05.936",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/8ab5c76a-eefb-4801-817f-458f68958db7/DreamShaperV6_a_masterpiece_image_of_Splash_art_music_album_ar_6.jpg",
                    "id": "e7a9a1ff-76be-4cbd-b560-7379f1af2c32",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a warrior fighting a dragon",
                        "generated_images": [
                            {
                                "id": "b1c9e57c-acf1-442b-9669-6a34d5128fb7",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/0ca698f0-9623-4081-93e0-e2516fb0d3bd/DreamShaperV6_a_warrior_fighting_a_dragon_4.jpg",
                                "likeCount": 14,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "d2fb9cf9-7999-4ae5-8bfe-f0df2d32abf8",
                "name": "DreamShaper v5",
                "description": "A versatile model great at both photorealism and anime, includes noise offset training, by Lykon.",
                "instancePrompt": None,
                "modelHeight": 832,
                "modelWidth": 640,
                "coreModel": "SD",
                "createdAt": "2023-04-13T04:56:36.796",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/bb22942b-40c8-4a06-a219-238808053ee0/DreamShaper_v5_extremely_intricate_fantasy_character_photoreal_0.jpg",
                    "id": "27bec45f-b450-4775-817f-761683f2cc5e",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "extremely intricate fantasy character, photorealistic, portrait of a great warrior, intricate details on clothing, professional oil painting, deviantart hd, artstation hd, concept art, cg society, dramatic, award winning matte drawing cinematic lighting octane render unreal engine volumetrics dtx",
                        "generated_images": [
                            {
                                "id": "0e0394bb-c1e7-46f4-b6e4-b205f97ecec7",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/4aa70349-6456-4ef7-a942-8c3db37a8339/DreamShaper_v5_extremely_intricate_fantasy_character_photoreal_1.jpg",
                                "likeCount": 18,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "b820ea11-02bf-4652-97ae-9ac0cc00593d",
                "name": "Leonardo Diffusion",
                "description": "A model with incredible shading and contrast, great at both photos and artistic styles, by cac0e.",
                "instancePrompt": None,
                "modelHeight": 1024,
                "modelWidth": 1024,
                "coreModel": "SD",
                "createdAt": "2023-02-28T20:26:06.053",
                "sdVersion": "v2",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/8905a8f0-9219-43ad-8ecb-1c37b4501dc5/Leonardo_Diffusion_ultra_detailed_artistic_photography_of_a_fashion_moden_3.jpg",
                    "id": "08b6f797-85f1-457a-a194-2e82f725bd6b",
                    "__typename": "generated_images",
                },
                "imageCount": 5343,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "A stunning image of a Vulcan warrior",
                        "generated_images": [
                            {
                                "id": "14bcb95a-a52a-4dd0-837c-c782ab065d8f",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/bb70ebcb-48fe-488b-b220-fb19696b385e/Leonardo_Diffusion_A_stunning_image_of_a_Vulcan_warrior_2.jpg",
                                "likeCount": 4,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "a097c2df-8f0c-4029-ae0f-8fd349055e61",
                "name": "RPG 4.0",
                "description": "This model is best at creating RPG character portraits with the ability for great photorealism. Created by Anashel.",
                "instancePrompt": None,
                "modelHeight": 832,
                "modelWidth": 640,
                "coreModel": "SD",
                "createdAt": "2023-02-09T11:47:04.271",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/20cd8cca-ad36-46b1-a0e3-8bd669112017/RPG_portrait_painting_of_a_redhead_feminine_royal_woman_with_a_fe_3.jpg",
                    "id": "419e4e5e-245d-49f0-b613-b1e8b02f6ca5",
                    "__typename": "generated_images",
                },
                "imageCount": 1000070,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "Photography of a well built modern cottage house sitting on top of a lake covered in snow, sunset moment, surrounded by mountains, Unsplash contest winner, cozy interior, warm interior lighting, made of glass, Vray, minimalist, high details, denoise, insanely detailed and intricate, professional color graded, hyper realistic, super detailed, 8k,HDR,high-resolution DSLR photograph, shot on IMAX200",
                        "generated_images": [
                            {
                                "id": "1cd73660-1c9c-4409-b856-e5da0d30d003",
                                "url": "https://cdn.leonardo.ai/users/b35decec-845a-475a-960f-a690332c3cf3/generations/926c827d-3504-4541-b4ff-49c5f4487858/RPG_Photography_of_a_well_built_modern_cottage_house_sitting_on_t_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "458ecfff-f76c-402c-8b85-f09f6fb198de",
                "name": "Deliberate 1.1",
                "description": "A powerful model created by XpucT that  is great for both photorealism and artistic creations.",
                "instancePrompt": None,
                "modelHeight": 832,
                "modelWidth": 640,
                "coreModel": "SD",
                "createdAt": "2023-02-08T10:25:54.556",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/da624520-f0c6-4afa-b171-9bfc3bbb27de/Deliberate_v11_waitress_pinup_art_style_kodak_portra_400_cinematic_smiling_0.jpg",
                    "id": "59776f05-378e-4c95-88c0-1740ca6c25a3",
                    "__typename": "generated_images",
                },
                "imageCount": 1048521,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "High detail RAW color art, animation, cartoon, magical atmosphere, (detailed skin, skin texture), (intricately detailed, fine details, hyperdetailed), raytracing, subsurface scattering, (muted colors), diffused soft lighting, shallow depth of field, by (Oliver Wetter), photographed on a Canon EOS R5, 28mm lens, F/2.8, sharp focus bokeh, backlight, volumetric lighting, (by Anastasiya Dobrovolskaya)",
                        "generated_images": [
                            {
                                "id": "2a6793b4-8482-4026-8bf7-09151ab3159f",
                                "url": "https://cdn.leonardo.ai/users/2e1f21ed-7ca4-4f78-80ed-1646ea463a01/generations/ddf7239c-4972-429b-8a0a-1de6f9647738/Deliberate_High_detail_RAW_color_art_animation_cartoon_magical_atmospher_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "17e4edbf-690b-425d-a466-53c816f0de8a",
                "name": "Vintage Style Photography",
                "description": "This model can generate a broad range of imagery with a vintage style as if it was taken from a film camera",
                "instancePrompt": "vintage style",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-01-29T09:40:50.165",
                "sdVersion": "v2",
                "type": "PHOTOGRAPHY",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "4e397cdd-4af3-48e5-b0e7-c2b5d1ebee59", "username": "Jachin", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/4e397cdd-4af3-48e5-b0e7-c2b5d1ebee59/generations/7a6f17f3-689c-461d-9c59-14a7ac88fa0e/Vintage_Style_Photography_Classic_convertible_driving_on_an_open_road_vintage_style_2.jpg",
                    "id": "7ffe80b5-11d6-419b-89d1-25abe7cd3fd0",
                    "__typename": "generated_images",
                },
                "imageCount": 59908,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": " A vibrant, sun-drenched vintage-style street scene with a classic car parked in the foreground.",
                        "generated_images": [
                            {
                                "id": "c07a9677-2747-42c7-90fa-1638f36a08ea",
                                "url": "https://cdn.leonardo.ai/users/4e397cdd-4af3-48e5-b0e7-c2b5d1ebee59/generations/f49e35b6-0ed8-4fa7-a015-c3e59a0bd4a3/Vintage_v1_A_vibrant_sundrenched_vintagestyle_street_scene_with_a_clas_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "f3296a34-9aef-4370-ad18-88daf26862c3",
                "name": "DreamShaper 3.2",
                "description": "This model by Lykon is great at a range of portrait styles as well as artistic backgrounds.",
                "instancePrompt": None,
                "modelHeight": 832,
                "modelWidth": 640,
                "coreModel": "SD",
                "createdAt": "2023-01-23T11:21:17.532",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/b2919072-7c52-409e-9c2a-11d56c5c2ed2/DreamShaper_32_Full_body_Beautiful_final_fantasy_style_portrait_clean_detai_2.jpg",
                    "id": "758af0e6-ffcc-494a-9543-aa123612c968",
                    "__typename": "generated_images",
                },
                "imageCount": 856247,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "beautiful elve,dragon , portait, highly detailed, 8k",
                        "generated_images": [
                            {
                                "id": "43d66bae-8a8d-45c0-8b94-b252b556dc4c",
                                "url": "https://cdn.leonardo.ai/users/2e1f21ed-7ca4-4f78-80ed-1646ea463a01/generations/c315ef67-1b35-43da-8440-e2b802b1008a/DreamShaper_beautiful_elvedragon_portait_highly_detailed_8k_0.jpg",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "cd2b2a15-9760-4174-a5ff-4d2925057376",
                "name": "Leonardo Select",
                "description": "A powerful finetune of SD2.1 that can achieve a high level of realism.",
                "instancePrompt": None,
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-01-06T01:05:25.657",
                "sdVersion": "v2",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": None,
                "imageCount": 481673,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "portrait of female character wearing 80s clothing. she should look to the left. she should have blonde hair ",
                        "generated_images": [
                            {
                                "id": "5c1a4725-160d-49cb-9b91-4ad2ac3de9a8",
                                "url": "https://cdn.leonardo.ai/users/2e1f21ed-7ca4-4f78-80ed-1646ea463a01/generations/ff4e1c40-933a-47da-8c52-31689ed282d7/Leonardo_Select_portrait_of_female_character_wearing_80s_clothing_she_should_0.png",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "6bef9f1b-29cb-40c7-b9df-32b51c1f67d3",
                "name": "Leonardo Creative",
                "description": "An alternative finetune of SD 2.1 that brings a little more creative interpretation to the mix.",
                "instancePrompt": None,
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2023-01-06T01:02:38.315",
                "sdVersion": "v2",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": None,
                "imageCount": 2416039,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "portrait of male character wearing 80s clothing. he should look to the left. he should have blonde hair and a mustache",
                        "generated_images": [
                            {
                                "id": "d0841a38-0e78-4a84-acc7-62c669f8cf78",
                                "url": "https://cdn.leonardo.ai/users/2e1f21ed-7ca4-4f78-80ed-1646ea463a01/generations/3665e729-cf65-4766-aebc-e351bc27e239/Leonardo_Creative_portrait_of_male_character_wearing_80s_clothing_he_should_lo_0.png",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "47a6232a-1d49-4c95-83c3-2cc5342f82c7",
                "name": "Battle Axes",
                "description": "Generate a variety of detailed axe designs with this model. From medieval battle axes to modern chopping axes, this model is great for creating a r...",
                "instancePrompt": "Axe",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2022-12-30T12:20:12.519",
                "sdVersion": "v1_5",
                "type": "GAME_ITEMS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "4e397cdd-4af3-48e5-b0e7-c2b5d1ebee59", "username": "Jachin", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/4e397cdd-4af3-48e5-b0e7-c2b5d1ebee59/generations/1a60b46c-24d1-47c0-9683-e0e837b6f129/Battle_Axes_an_axe_blade_centre_of_frame_3.jpg",
                    "id": "29e709a4-00a0-48c1-af53-1d9640a6febd",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": " A menacing, jagged-edged axe with a glowing, fiery blade, perfect for a fantasy RPG.",
                        "generated_images": [
                            {
                                "id": "364f31e2-d337-40ad-bc5f-c683aea2cdf0",
                                "url": "https://cdn.leonardo.ai/users/4e397cdd-4af3-48e5-b0e7-c2b5d1ebee59/generations/f5e64c82-0d31-40fc-bb8b-3a4c273243d4/Default_A_menacing_jaggededged_axe_with_a_glowing_fiery_blade_perfec_0.png",
                                "likeCount": 1,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "e5a291b6-3990-495a-b1fa-7bd1864510a6",
                "name": "Pixel Art",
                "description": "A pixel art model that's trained on headshots, but is surprisingly flexible with all sorts of subjects.",
                "instancePrompt": "pixel art",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2022-12-30T06:21:16.301",
                "sdVersion": None,
                "type": "PIXEL_ART",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": None,
                "imageCount": 85083,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "A robotic cat with glowing eyes and sleek metal fur.",
                        "generated_images": [
                            {
                                "id": "b582fad8-9149-4733-9798-19ec5fb84393",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/5628b06f-d989-4f89-87b2-9f7af4bb0ee7/Default_A_robotic_cat_with_glowing_eyes_and_sleek_metal_fur_0.png",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "302e258f-29b5-4dd8-9a7c-0cd898cb2143",
                "name": "Chest Armor",
                "description": "Create all sorts of chest armor with this model in a consistent style but with wide thematic range.",
                "instancePrompt": "chest armor",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2022-12-29T21:13:02.608",
                "sdVersion": "v1_5",
                "type": "GAME_ITEMS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "test chest armor",
                        "generated_images": [
                            {
                                "id": "050cb02c-5122-4e97-9810-f784e6bb64c4",
                                "url": "https://cdn.leonardo.ai/users/2e1f21ed-7ca4-4f78-80ed-1646ea463a01/generations/465401c6-febf-4223-a9f1-fae4e54931bf/Default_test_chest_armor_2.png",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "102a8ee0-cf16-477c-8477-c76963a0d766",
                "name": "Crystal Deposits",
                "description": "A model for creating crystal deposits. Well-suited for use as items or in an isometric environment.",
                "instancePrompt": "a crystal",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2022-12-29T21:13:02.608",
                "sdVersion": "v1_5",
                "type": "ENVIRONMENTS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a yellow tkwst2, object, 2d object, art by tekkonkinkreet, octane render, unreal engine, 3D, 8K, ultra-detailed, intricate, sharp focus",
                        "generated_images": [
                            {
                                "id": "f7542346-c640-40ba-9f51-453e1cea3020",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/a9c191fa-6137-4e01-922c-943ee4e4788c/Default_a_yellow_tkwst2_object_2d_object_art_by_tekkonkinkreet_octane_2.png",
                                "likeCount": 2,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "45ab2421-87de-44c8-a07c-3b87e3bfdf84",
                "name": "Magic Potions",
                "description": 'A great model for creating incredible semi-realistic magic potions. Try appending "intricately detailed, 3d vray render" to your prompt.',
                "instancePrompt": "a magic potion",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2022-12-29T21:13:02.608",
                "sdVersion": "v1_5",
                "type": "GAME_ITEMS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/6ae64207-79bc-48e2-b721-46c00d8c938b/Default_a_stunningly_beautiful_magic_potion_containing_a_galaxy_fili_1.png",
                    "id": "3aa11a5c-0496-40ca-b635-e3c78f161666",
                    "__typename": "generated_images",
                },
                "imageCount": 15026,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a stunning magic potion, intricately detailed, 3d vray render",
                        "generated_images": [
                            {
                                "id": "a7303236-34f8-4ce7-a187-a95966b858ff",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/8765c4f3-55ed-40c0-9aeb-778f54ee27ab/Default_a_stunning_magic_potion_intricately_detailed_3d_vray_render_3.png",
                                "likeCount": 3,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "6c95de60-a0bc-4f90-b637-ee8971caf3b0",
                "name": "Character Portraits",
                "description": "A model that's for creating awesome RPG characters of varying classes in a consistent style.",
                "instancePrompt": "character portrait",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2022-12-29T21:13:02.608",
                "sdVersion": "v1_5",
                "type": "CHARACTERS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "male king, green hair, detailed, soft, hyper-detailed, Cinematic, octane render",
                        "generated_images": [
                            {
                                "id": "df6c66b3-882d-4303-8bb2-e8073c2e677b",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/1d554364-792b-498a-be17-ea0dfcca67d1/Default_male_king_green_hair_detailed_soft_hyperdetailed_Cinematic_oc_0.png",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "2d18c0af-374e-4391-9ca2-639f59837c85",
                "name": "Magic Items",
                "description": "Create a wide range of magical items like weapons, shields, boots, books. Very versatile.",
                "instancePrompt": "an item",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2022-12-29T21:13:02.608",
                "sdVersion": "v1_5",
                "type": "GAME_ITEMS",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a red boot, object, concept art, dota 2 style, red abstract background, watercolor, epic smooth illustration",
                        "generated_images": [
                            {
                                "id": "66dfe54f-2a56-49d7-b5aa-04ad012a9293",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/1a2ce3b1-998c-4795-8582-6f49aca28160/Default_a_red_boot_object_concept_art_dota_2_style_red_abstract_backg_1.png",
                                "likeCount": 3,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "ff883b60-9040-4c18-8d4e-ba7522c6b71d",
                "name": "Amulets",
                "description": "Create unique and intricate amulets, jewellery and more. Try loading up the prompt terms to steer it in interesting directions.",
                "instancePrompt": "an amulet",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2022-12-28T20:31:20",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": " A close-up of an ancient amulet, illuminated by a single ray of light from a nearby window.",
                        "generated_images": [
                            {
                                "id": "b68004dd-c030-4e51-8e68-d9638506e15a",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/edccace2-4291-482b-b3c6-d735ff06e640/Default_A_closeup_of_an_ancient_amulet_illuminated_by_a_single_ray_o_2.png",
                                "likeCount": 1,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "4b2e0f95-f15e-48d8-ada3-c071d6104db8",
                "name": "Christmas Stickers",
                "description": "Generate festive and fun Christmas stickers with this model. From cute and colorful to traditional and elegant.",
                "instancePrompt": "a sticker",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2022-12-28T20:31:20",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "test sticker",
                        "generated_images": [
                            {
                                "id": "3c737702-f32e-4dc0-b2d6-6e8a9a036be5",
                                "url": "https://cdn.leonardo.ai/users/2e1f21ed-7ca4-4f78-80ed-1646ea463a01/generations/15aaa53a-6ee1-4887-bfba-f00213f64756/Default_test_sticker_0.png",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "50c4f43b-f086-4838-bcac-820406244cec",
                "name": "Cute Characters",
                "description": 'Create cute and charming game characters, perfect for adding some whimsy to your game design. Be sure to include the word "character" in your prompts for best results.',
                "instancePrompt": "a character",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2022-12-28T20:31:20",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": None,
                "imageCount": 45280,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "A zany game character clad in an outrageous cowboy grass skirt, wild paisley jacket, and light-up sneakers.",
                        "generated_images": [
                            {
                                "id": "68ed1341-ea92-4637-9bb9-237432628c13",
                                "url": "https://cdn.leonardo.ai/users/4e397cdd-4af3-48e5-b0e7-c2b5d1ebee59/generations/85cf7bd8-a233-42ca-a7d0-e900a0bdbb2a/Default_A_zany_game_character_clad_in_an_outrageous_cowboy_grass_skir_1.png",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "6908bfaf-8cf2-4fda-8c46-03f892d82e06",
                "name": "Cute Animal Characters",
                "description": "Perfect for creating adorable and cute animal characters - loveable and playful designs.",
                "instancePrompt": "a character",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2022-12-28T20:31:20",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": None,
                "imageCount": 96633,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a rabbit character",
                        "generated_images": [
                            {
                                "id": "de3da9e6-eab2-4306-a336-43edce4b00b0",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/6ac55e1f-500a-4967-bf7e-e5af117c5f6d/Default_a_rabbit_character_0.png",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "5fdadebb-17ae-472c-bf76-877e657f97de",
                "name": "Spirit Creatures",
                "description": "From whimsical fairy-like beings to mythical creatures, create unique cute spirit characters.",
                "instancePrompt": "a creature",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2022-12-28T20:31:20",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a creature with more than six eyes in rainbow colors",
                        "generated_images": [
                            {
                                "id": "f9e470bc-7fd3-4472-ae77-c1c09eb8f5d5",
                                "url": "https://cdn.leonardo.ai/users/7a129367-fa22-48ff-a5eb-441861c60a20/generations/8874bdc9-9e80-4acb-ae5a-fa2c4db6819b/Default_a_creature_with_more_than_six_eyes_in_rainbow_colors_0.png",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "ab200606-5d09-4e1e-9050-0b05b839e944",
                "name": "Isometric Fantasy",
                "description": 'Create all sorts of isometric fantasy environments. Try appending "3d vray render, isometric" and using a guidance scale of 6. For the negative prompt, try "unclear, harsh, oversaturated, soft, blurry".',
                "instancePrompt": "isometric fantasy",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2022-12-28T20:31:20",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": {
                    "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/8f5f48d1-0042-4625-b47a-83e266432abf/Isometric_Fantasy_Waterfall_isolated_on_white_3d_vray_render_isometric_ultra_d_3.jpg",
                    "id": "8aa79ad7-dca0-4d88-9b8b-e4766e1e9047",
                    "__typename": "generated_images",
                },
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a fantasy diorama with a castle and lake",
                        "generated_images": [
                            {
                                "id": "9eeddd56-fd49-4805-8c37-4ee03ddbc5f1",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/9f8ee7a6-e5b9-4fe1-9a14-77d7f44ad4e1/Default_a_fantasy_diorama_with_a_castle_and_lake_0.png",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "ee0fc1a3-aacb-48bf-9234-ada3cc02748f",
                "name": "Shields",
                "description": "Create a variety of impressively varied and detailed shield designs. Allows for an incredible range of material types.",
                "instancePrompt": "a shield",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2022-12-28T20:31:20",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "An extraterrestrial shield bearing delicate swirls and ethereal filigrees",
                        "generated_images": [
                            {
                                "id": "da79e8e6-2bd1-4022-82c4-f21127bbc3fc",
                                "url": "https://cdn.leonardo.ai/users/4e397cdd-4af3-48e5-b0e7-c2b5d1ebee59/generations/7b3c338c-8011-42e7-bcc7-4c9cfd450b71/Default_An_extraterrestrial_shield_bearing_delicate_swirls_and_ethere_1.png",
                                "likeCount": 1,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "7a65f0ab-64a7-4be2-bcf3-64a1cc56f627",
                "name": "Isometric Scifi Buildings",
                "description": 'Great at creating scifi buildings of varying themes. Append the word isometric to your prompt to ensure an isometric view. "3d vray render" also helps steer the generation well. ',
                "instancePrompt": "isometric scifi",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2022-12-28T20:31:20",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a stunning scifi base, turrets and lasers, 3d vray render",
                        "generated_images": [
                            {
                                "id": "08cf2772-080e-4220-ac97-91cc13f18e61",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/1aa5f16a-b64e-4a41-98d2-702fae7d4ba2/Default_a_stunning_scifi_base_turrets_and_lasers_3d_vray_render_0.png",
                                "likeCount": 1,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "5fce4543-8e23-4b77-9c3f-202b3f1c211e",
                "name": "Crystal Deposits Alternate",
                "description": 'An alternative crystal deposits model that gives a slightly more realistic feel with its creations. Try using "object" and "3d vray render" in your prompts.',
                "instancePrompt": "1@t crystal",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2022-12-28T14:41:59.451",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "a crystal",
                        "generated_images": [
                            {
                                "id": "510a3f3c-542d-4d6b-8c49-b3e0cf82e44a",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/49c5c8a5-5fd9-4222-bc15-6ac8cd63cb8e/Default_a_crystal_3.png",
                                "likeCount": 2,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "756be0a8-38b1-4946-ad62-c0ac832422e3",
                "name": "Isometric Asteroid Tiles",
                "description": 'A model for creating isometric asteroid environment tiles. Try appending "3d vray render, unreal engine, beautiful, intricately detailed, trending on artstation, 8k" to your prompt.',
                "instancePrompt": "1@t isometric asteroid",
                "modelHeight": 512,
                "modelWidth": 512,
                "coreModel": "SD",
                "createdAt": "2022-12-28T06:54:35.42",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": None,
                "imageCount": 0,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "isometric tile, 3d vray render, unreal engine, beautiful, intricately detailed, trending on artstation, 8k",
                        "generated_images": [
                            {
                                "id": "1b5c1821-9ebf-4fea-867f-58e847c0995e",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/8cd48839-28fe-4f25-9a32-b7a8a118583b/Default_isometric_tile_3d_vray_render_unreal_engine_beautiful_intrica_0.png",
                                "likeCount": 0,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
            {
                "id": "291be633-cb24-434f-898f-e662799936ad",
                "name": "Leonardo Signature",
                "description": "The core model of the Leonardo platform. An extremely powerful and diverse finetune which is highly effective for a wide range of uses.",
                "instancePrompt": "",
                "modelHeight": 768,
                "modelWidth": 768,
                "coreModel": "SD",
                "createdAt": "2022-12-24T21:08:03.749",
                "sdVersion": "v1_5",
                "type": "GENERAL",
                "nsfw": False,
                "public": True,
                "trainingStrength": "MEDIUM",
                "user": {"id": "384ab5c8-55d8-47a1-be22-6a274913c324", "username": "Leonardo", "__typename": "users"},
                "generated_image": None,
                "imageCount": 864451,
                "__typename": "custom_models",
                "generations": [
                    {
                        "prompt": "an incredibly stunning photograph of a throne room, soft lighting",
                        "generated_images": [
                            {
                                "id": "eec2d87e-d27c-4b95-8a1a-b948fd49df1e",
                                "url": "https://cdn.leonardo.ai/users/384ab5c8-55d8-47a1-be22-6a274913c324/generations/2956bf2a-3039-43ee-83d6-65318e5f58fa/Default_an_incredibly_stunning_photograph_of_a_throne_room_soft_light_2.png",
                                "likeCount": 122,
                                "__typename": "generated_images",
                            }
                        ],
                        "__typename": "generations",
                    }
                ],
                "user_favourite_custom_models": [],
            },
        ]
    }
}
