# DeepOptimizeSpaceProgress（系统接口）

Defines the DeepOptimizeSpaceProgress data structure.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-photoAccessHelper-interface DeepOptimizeSpaceProgress--><!--Device-photoAccessHelper-interface DeepOptimizeSpaceProgress-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## progress

```TypeScript
progress: int
```

The percentage of deep optimize space state.Unit: Percentage, The value range is all integers, Value range: [0, 100].

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DeepOptimizeSpaceProgress-progress: int--><!--Device-DeepOptimizeSpaceProgress-progress: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## state

```TypeScript
state: DeepOptimizeState
```

The current deep optimize space state.

**类型：** [DeepOptimizeState](arkts-medialibrary-photoaccesshelper-deepoptimizestate-e-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DeepOptimizeSpaceProgress-state: DeepOptimizeState--><!--Device-DeepOptimizeSpaceProgress-state: DeepOptimizeState-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

