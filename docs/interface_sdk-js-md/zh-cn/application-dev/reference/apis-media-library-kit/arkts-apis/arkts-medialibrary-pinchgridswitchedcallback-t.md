# PinchGridSwitchedCallback

```TypeScript
export type PinchGridSwitchedCallback = (gridLevel: photoAccessHelper.GridLevel) => void
```

Callback to be invoked when a user pinches a grid component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export type PinchGridSwitchedCallback = (gridLevel: photoAccessHelper.GridLevel) => void--><!--Device-unnamed-export type PinchGridSwitchedCallback = (gridLevel: photoAccessHelper.GridLevel) => void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| gridLevel | photoAccessHelper.GridLevel | 是 | Number of columns in the grid. |

