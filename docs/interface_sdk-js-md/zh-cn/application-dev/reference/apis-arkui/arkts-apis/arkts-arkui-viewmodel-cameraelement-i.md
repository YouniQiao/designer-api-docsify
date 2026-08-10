# CameraElement

The &lt;camera&gt; component provides preview and photographing functions.

**继承/实现关系：** CameraElement extends [Element](arkts-arkui-viewmodel-element-i.md)

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

<!--Device-unnamed-export interface CameraElement extends Element--><!--Device-unnamed-export interface CameraElement extends Element-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## takePhoto

```TypeScript
takePhoto(options: CameraTakePhotoOptions): void
```

Take photos with specified parameters.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-CameraElement-takePhoto(options: CameraTakePhotoOptions): void--><!--Device-CameraElement-takePhoto(options: CameraTakePhotoOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CameraTakePhotoOptions](arkts-arkui-viewmodel-cameratakephotooptions-i.md) | 是 | the parameters of camera. |

