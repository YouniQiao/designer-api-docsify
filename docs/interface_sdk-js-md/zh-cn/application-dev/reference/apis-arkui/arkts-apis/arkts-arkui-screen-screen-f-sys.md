# Screen（系统接口）

## Screen

```TypeScript
export declare function Screen(
   screenId: long,
   content_?: CustomBuilder,
): ScreenAttribute
```

Defines Screen Component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function Screen(   screenId: long,   content_?: CustomBuilder,): ScreenAttribute--><!--Device-unnamed-export declare function Screen(   screenId: long,   content_?: CustomBuilder,): ScreenAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| screenId | long | 是 | screenId |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScreenAttribute](../arkts-components/arkts-arkui-screen-attribute.md) |  |

