# commonEventSubscribeInfo(The CommonEventSubscribeInfo module provides APIs for providing subscriber information.)

/*
 Copyright (c) 2021-2023 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [CommonEventSubscribeInfo](arkts-basicservices-commoneventsubscribeinfo-commoneventsubscribeinfo-i.md) | This module provides APIs for providing subscriber information. It allows you to configure parameters such as the subscribed common event type, publisher permission, publisher device ID, user ID, and subscription priority. This module is applicable to scenarios where an app needs to subscribe to system common events or custom common events and requires refined control over event sources. > **NOTE：**> > After users subscribing to custom common events, any application can send potential > malicious common events to subscribers. The **publisherPermission** and > **publisherBundleName** parameters of this module can be used to restrict the publisher > scope of common events. |

