# https://tools.shajon.dev/curl-converter | By SHAJON-404

import requests
import json

url = 'https://b-graph.facebook.com/graphql'

headers = {
    "x-fb-request-analytics-tags": json.dumps({
        "network_tags": {
            "product": "121876164619130",
            "request_category": "graphql",
            "purpose": "fetch",
            "retry_attempt": "0",
        },
        "application_tags": "graphservice",
    }, separators=(',', ':')),
    "x-fb-connection-type": "dummy",
    "app-scope-id-header": "2e8d1264-da5f-44ef-9f5f-06af11ff3c8a",
    "x-zero-state": "unknown",
    "authorization": "OAuth 121876164619130|1ab2c5c902faedd339c14b2d58e929dc",
    "x-zero-eh": "664c0faaac849cb891d0a261fbb72a12",
    "content-type": "application/x-www-form-urlencoded",
    "x-graphql-client-library": "graphservice",
    "x-graphql-request-purpose": "fetch",
    "x-tigon-is-retry": "False",
    "x-fb-friendly-name": "com.bloks.www.bloks.caa.login.async.send_login_request",
    "user-agent": "[FBAN/PAAA;FBAV/564.0.0.34.103;FBDM/{density=2.7250001,width=1080,height=2292};FBLC/en_US;FBBV/1026477462;FB_FW/2;FBSN/Android;FBDI/null;FBCR/null;FBMF/TECNO;FBBD/TECNO;FBDV/TECNO CK7n;FBSV/14;FBCA/arm64-v8a:null;]",
    "x-fb-http-engine": "Tigon/Liger",
    "x-fb-client-ip": "True",
    "x-fb-server-cluster": "True",
    "x-fb-conn-uuid-client": "3aex6R7nQ06fyUJgDHDRwA==",
}

data = {
    "method": "post",
    "format": "json",
    "server_timestamps": "true",
    "locale": "en_US",
    "purpose": "fetch",
    "fb_api_req_friendly_name": "com.bloks.www.bloks.caa.login.async.send_login_request",
    "fb_api_caller_class": "graphservice",
    "client_doc_id": "11994080426599066514545155208",
    "fb_api_client_context": json.dumps({
        "is_background": False,
    }, separators=(',', ':')),
    "variables": json.dumps({
        "params": {
            "params": json.dumps({
                "params": json.dumps({
                    "client_input_params": {
                        "blocked_uids": [],
                        "aac": json.dumps({
                            "aac_init_timestamp": 1785680928,
                            "aacjid": "a612cc1a-85f3-4129-bdda-82ae2d7c9f38",
                            "aaccs": "kWsKBV0V6uPv7lJLY6FuSR9Sdhr-hvy-wHTWrEoXJnI",
                        }, separators=(',', ':')),
                        "sim_phones": [
                            "",
                        ],
                        "aymh_accounts": [],
                        "network_bssid": None,
                        "secure_family_device_id": "",
                        "has_granted_read_contacts_permissions": 0,
                        "auth_secure_device_id": "",
                        "has_whatsapp_installed": 1,
                        "password": "#PWD_ENC:2:1785680953:AejHB1H4x/ndHzmzzRMAAaFIsEcMfKLy6PKf3Uet6A32EoEpBZuLUphED5X6HG86f4By69Q21990bEIK5HANc6t8iJcJowdZFp5UZMRFVkVOSmplFu4j8f94mAnFUdS+Sp1f2f3yT6WOooFNhektMqUFCvdajgO4lf4czl6AHWizbvPuZI6xipngZd95WyCqPm9HK7rrfY08+VLrQ4LRUbCgvhHla4VyoSfVyUOeTEF68s2ALEZJ9NHyGEvMHBgpqWsm37idc4Z9qRL6CdBEC63ycDVqR4Xqiz7n6ugyt5mgqvLnGUXm9NpTapHKXu4ZF6FTRS/ojBvmQ0qqxX4+iEH2jy5DGvdUfw6UGXxHR0/HUsoj9bqPij0c6nEjbDR1gtbi6FiR",
                        "sso_token_map_json_string": "",
                        "block_store_machine_id": "",
                        "cloud_trust_token": None,
                        "event_flow": "login_manual",
                        "password_contains_non_ascii": "false",
                        "client_known_key_hash": "",
                        "sso_accounts_auth_data": [],
                        "encrypted_msisdn": "",
                        "has_granted_read_phone_permissions": 0,
                        "app_manager_id": "",
                        "should_show_nested_nta_from_aymh": 0,
                        "zero_balance_state": "",
                        "login_attempt_count": 1,
                        "machine_id": "",
                        "accounts_list": [],
                        "gms_incoming_call_retriever_eligibility": "client_not_supported",
                        "fb_ig_device_id": [],
                        "device_emails": [],
                        "try_num": 1,
                        "lois_settings": {
                            "lois_token": "",
                        },
                        "event_step": "home_page",
                        "headers_infra_flow_id": "",
                        "openid_tokens": {},
                        "contact_point": "fuck. zuckk",
                    },
                    "server_params": {
                        "should_trigger_override_login_2fa_action": 0,
                        "is_from_logged_out": 0,
                        "should_trigger_override_login_success_action": 0,
                        "login_credential_type": "none",
                        "server_login_source": "login",
                        "waterfall_id": "c644b2e5-e22a-4437-a80b-c734d8e90869",
                        "two_step_login_type": "one_step_login",
                        "login_source": "Login",
                        "is_platform_login": 1,
                        "login_entry_point": "logged_out",
                        "INTERNAL__latency_qpl_marker_id": 36707139,
                        "is_from_aymh": 0,
                        "offline_experiment_group": "caa_iteration_v6_perf_fb_2",
                        "is_from_landing_page": 0,
                        "left_nav_button_action": "NONE",
                        "password_text_input_id": "wbjpc0:57",
                        "is_from_empty_password": 0,
                        "is_from_msplit_fallback": 0,
                        "ar_event_source": "login_home_page",
                        "username_text_input_id": "wbjpc0:56",
                        "layered_homepage_experiment_group": None,
                        "device_id": "2e8d1264-da5f-44ef-9f5f-06af11ff3c8a",
                        "login_surface": "login_home",
                        "INTERNAL__latency_qpl_instance_id": 195431270400229,
                        "reg_flow_source": "login_home_native_integration_point",
                        "is_caa_perf_enabled": 1,
                        "credential_type": "password",
                        "is_from_password_entry_page": 0,
                        "caller": "gslr",
                        "family_device_id": "e8ea88fd-1ddc-4ea5-8e8b-e63b7e1c8018",
                        "is_from_assistive_id": 0,
                        "access_flow_version": "pre_mt_behavior",
                        "is_from_logged_in_switcher": 0,
                    },
                }, separators=(',', ':')),
            }, separators=(',', ':')),
            "bloks_versioning_id": "7b85fbda1398538bd2a202cff7c08d417461eebcab92448db350e88a00e5e389",
            "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request",
        },
        "scale": "3",
        "nt_context": {
            "using_white_navbar": True,
            "styles_id": "dd4bbd884c6f98a954b86a57750c35df",
            "pixel_ratio": 3,
            "is_push_on": True,
            "is_flipper_enabled": False,
            "android_device_performance_class": 0,
            "debug_tooling_metadata_token": None,
            "gpu_memory_mb": 7655,
            "theme_params": [
                {
                    "value": [
                        "three_neutral_gray",
                    ],
                    "design_system_name": "XMDS",
                },
                {
                    "value": [],
                    "design_system_name": "FDS",
                },
            ],
            "bloks_version": "7b85fbda1398538bd2a202cff7c08d417461eebcab92448db350e88a00e5e389",
            "android_os_api_level": 34,
        },
    }, separators=(',', ':')),
    "fb_api_analytics_tags": json.dumps([
        "GraphServices",
    ], separators=(',', ':')),
    "client_trace_id": "7b654bec-e396-46c6-b2a5-e736b27fec5b",
}

response = requests.post(url, headers=headers, data=data)
print(f"Response Status Code: {response.status_code}")
print(f"Response Body: {response.text}")