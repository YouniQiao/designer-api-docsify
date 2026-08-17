# @ohos.multimodalInput.infraredEmitter(IR Management)

/*
 Copyright (c) 2024 Huawei Device Co., Ltd.
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

<!--Device-unnamed-declare namespace infraredEmitter--><!--Device-unnamed-declare namespace infraredEmitter-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InfraredEmitter

## Modules to Import

```TypeScript
import { infraredEmitter } from 'infraredEmitter';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [hasIrEmitter](arkts-input-infraredemitter-hasiremitter-f.md#hasiremitter) | Checks whether the device has an infrared transmitter. This API uses a promise to return the result. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getInfraredFrequencies](arkts-input-infraredemitter-getinfraredfrequencies-f-sys.md#getinfraredfrequencies) | Queries the frequency range of IR signals supported by the device. |
| [transmitInfrared](arkts-input-infraredemitter-transmitinfrared-f-sys.md#transmitinfrared) | Generates IR signals at the specified frequency and level. |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [InfraredFrequency](arkts-input-infraredemitter-infraredfrequency-i-sys.md) | Defines the frequency range of IR signals. |
<!--DelEnd-->

