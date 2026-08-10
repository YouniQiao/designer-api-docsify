# ReadingScreenPermissionStatus（系统接口）

Returns the status of the permission for reading screen information.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-onScreen-export interface ReadingScreenPermissionStatus--><!--Device-onScreen-export interface ReadingScreenPermissionStatus-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { onScreen } from 'kits/@kit.MultimodalAwarenessKit';
```

## readingCode

```TypeScript
readingCode?: int
```

If the screen information cannot be read, the corresponding status code will be returned.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadingScreenPermissionStatus-readingCode?: int--><!--Device-ReadingScreenPermissionStatus-readingCode?: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## readingState

```TypeScript
readingState: int
```

Whether screen reading is allowed. **0**: no; **1**: yes.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReadingScreenPermissionStatus-readingState: int--><!--Device-ReadingScreenPermissionStatus-readingState: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

