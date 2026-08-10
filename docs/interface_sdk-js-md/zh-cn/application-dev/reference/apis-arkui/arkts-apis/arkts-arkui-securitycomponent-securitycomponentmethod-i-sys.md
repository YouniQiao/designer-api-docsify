# SecurityComponentMethod

Declares the interface for the method of a security component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface SecurityComponentMethod--><!--Device-unnamed-export declare interface SecurityComponentMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## key

```TypeScript
key(value: string | undefined): this
```

Key. User can set an key to the component to identify it.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SecurityComponentMethod-key(value: string | undefined): this--><!--Device-SecurityComponentMethod-key(value: string | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string \| undefined | 是 | identify the key of the component. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | Returns the attribute of the security component. |

