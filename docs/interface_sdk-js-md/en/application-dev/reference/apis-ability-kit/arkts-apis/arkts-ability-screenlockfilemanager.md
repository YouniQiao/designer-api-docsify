# @ohos.ability.screenLockFileManager(Sensitive Data Access Management Under Lock Screen)

/*
 Copyright (C) 2024-2026 Huawei Device Co., Ltd.
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


**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace screenLockFileManager--><!--Device-unnamed-declare namespace screenLockFileManager-End-->

**System capability:** SystemCapability.Security.ScreenLockFileManager

## Modules to Import

```TypeScript
import { screenLockFileManager } from 'screenLockFileManager';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [acquireAccess](arkts-ability-screenlockfilemanager-acquireaccess-f.md#acquireAccess) | Requests the access permission for the caller app's sensitive data under the lock screen in synchronous mode. After the request is successful, the reference count of the sensitive data key increases, preventing the key from being destroyed after the screen has been locked for a duration reaching the system-configured lock duration threshold. This method must be used in pair with [releaseAccess](arkts-ability-screenlockfilemanager-releaseaccess-f.md#releaseAccess). Before calling this API, ensure that the app has enabled the sensitive data protection function under the lock screen, and that the key status queried through the [queryAppKeyState](arkts-ability-screenlockfilemanager-queryappkeystate-f.md#queryAppKeyState) API is KEY_EXIST. |
| [queryAppKeyState](arkts-ability-screenlockfilemanager-queryappkeystate-f.md#queryAppKeyState) | Queries the status of the caller app's sensitive data key under the lock screen in synchronous mode. |
| [releaseAccess](arkts-ability-screenlockfilemanager-releaseaccess-f.md#releaseAccess) | Releases the access permission for the caller app's sensitive data under the lock screen in synchronous mode. After the release is successful, the reference count of the sensitive data key decreases. When the count reaches zero, the key can be destroyed after the screen has been locked for a duration reaching the system-configured lock duration threshold. Before calling this API, ensure that the app has enabled the sensitive data protection function under the lock screen, and that the [acquireAccess](arkts-ability-screenlockfilemanager-acquireaccess-f.md#acquireAccess) API has been called to request the permission successfully first. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [acquireAccess](arkts-ability-screenlockfilemanager-acquireaccess-f-sys.md#acquireAccess-(System-API)) | Requests the permission to access a specified type of sensitive data under the lock screen synchronously. After the request is successful, the reference count of the sensitive data key increases, preventing the key from being destroyed after the screen has been locked for the system-configured duration threshold. This method must be used in pair with [releaseAccess](arkts-ability-screenlockfilemanager-releaseaccess-f.md#releaseAccess). Before calling this API, ensure that the app has enabled the sensitive data protection under lock screen feature and that the key state queried through the [queryAppKeyState](arkts-ability-screenlockfilemanager-queryappkeystate-f.md#queryAppKeyState) API is KEY_EXIST. |
| [queryAppKeyState](arkts-ability-screenlockfilemanager-queryappkeystate-f-sys.md#queryAppKeyState-(System-API)) | Queries the status of a specified type of sensitive data key under the lock screen synchronously. |
| [releaseAccess](arkts-ability-screenlockfilemanager-releaseaccess-f-sys.md#releaseAccess-(System-API)) | Releases the permission to access a specified type of sensitive data under the lock screen synchronously. After the release is successful, the reference count of the sensitive data key decreases. When the reference count reaches zero, the key can be destroyed after the screen has been locked for the system-configured duration threshold. Before calling this API, ensure that the app has enabled the sensitive data protection under lock screen feature and that the permission has been successfully requested by calling the [acquireAccess](arkts-ability-screenlockfilemanager-acquireaccess-f.md#acquireAccess) API first. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [AccessStatus](arkts-ability-screenlockfilemanager-accessstatus-e.md) | Enumerates the statuses for requesting access permissions for sensitive data under the lock screen. |
| [DataType](arkts-ability-screenlockfilemanager-datatype-e.md) | Enumerates the types of sensitive data that can be accessed under the lock screen. |
| [KeyStatus](arkts-ability-screenlockfilemanager-keystatus-e.md) | Enumerates the statuses of sensitive data keys under the lock screen. |
| [ReleaseStatus](arkts-ability-screenlockfilemanager-releasestatus-e.md) | Enumerates the statuses for releasing access permissions for sensitive data under the lock screen. |

