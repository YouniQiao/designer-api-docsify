# TypeConstructorWithArgs

含有任意入参的类构造器。

**起始版本：** 12

**废弃版本：** -1

<!--Device-unnamed-export interface TypeConstructorWithArgs--><!--Device-unnamed-export interface TypeConstructorWithArgs-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
new(...args: any): T
```

创建并返回一个指定类型T的实例。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-TypeConstructorWithArgs-new(...args: any): T--><!--Device-TypeConstructorWithArgs-new(...args: any): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | any | 是 |

**返回值：**

| 类型 |
| --- |
| T |
