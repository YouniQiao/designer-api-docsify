# RootScene（系统接口）

## RootScene

```TypeScript
export declare function RootScene(
    session: RootSceneSession,
    content_?: CustomBuilder,
): RootSceneAttribute
```

Defines the RootScene Component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function RootScene(    session: RootSceneSession,    content_?: CustomBuilder,): RootSceneAttribute--><!--Device-unnamed-export declare function RootScene(    session: RootSceneSession,    content_?: CustomBuilder,): RootSceneAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| session | [RootSceneSession](arkts-arkui-rootscene-rootscenesession-i.md) | 是 |  |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RootSceneAttribute](../arkts-components/arkts-arkui-rootscene-attribute.md) |  |

