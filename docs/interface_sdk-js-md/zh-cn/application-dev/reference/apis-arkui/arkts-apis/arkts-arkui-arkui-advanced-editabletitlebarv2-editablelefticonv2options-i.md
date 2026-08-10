# EditableLeftIconV2Options

左侧图标配置选项接口。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export declare interface EditableLeftIconV2Options--><!--Device-unnamed-export declare interface EditableLeftIconV2Options-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { EditableSaveButtonV2, EditableTitleBarStyleV2Options, EditableTitleBarStyleV2, EditableTitleBarItemV2, EditableLeftIconV2Options, EditableTitleBarMenuItemV2, EditableTitleBarV2, EditableTitleBarMenuItemV2Options, EditableSaveButtonV2Options, EditableTitleBarItemV2Options, EditableTitleV2Options, EditableTitleV2, EditableLeftIconV2, EditableLeftIconTypeV2 } from 'kits/@kit.ArkUI';
```

## onAction

```TypeScript
onAction?: OnActionCallback
```

点击左侧图标的回调函数。未设置时，Back类型默认执行路由返回，Cancel类型无操作。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EditableLeftIconV2Options-onAction?: OnActionCallback--><!--Device-EditableLeftIconV2Options-onAction?: OnActionCallback-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## defaultFocus

```TypeScript
defaultFocus?: boolean
```

是否默认获取焦点。

true：获焦。

false：不获焦。

默认值：false。

**类型：** boolean

**默认值：** false

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EditableLeftIconV2Options-defaultFocus?: boolean--><!--Device-EditableLeftIconV2Options-defaultFocus?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## iconType

```TypeScript
iconType?: EditableLeftIconTypeV2
```

图标类型。

**类型：** [EditableLeftIconTypeV2](arkts-arkui-arkui-advanced-editabletitlebarv2-editablelefticontypev2-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EditableLeftIconV2Options-iconType?: EditableLeftIconTypeV2--><!--Device-EditableLeftIconV2Options-iconType?: EditableLeftIconTypeV2-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

