# WindowScene（系统接口）

## WindowScene

```TypeScript
export declare function WindowScene(
    persistentId: int,
    content_?: CustomBuilder,
): WindowSceneAttribute
```

Defines the WindowScene Component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function WindowScene(    persistentId: int,    content_?: CustomBuilder,): WindowSceneAttribute--><!--Device-unnamed-export declare function WindowScene(    persistentId: int,    content_?: CustomBuilder,): WindowSceneAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| persistentId | int | 是 |  |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WindowSceneAttribute](../arkts-components/arkts-arkui-windowscene-attribute.md) |  |

