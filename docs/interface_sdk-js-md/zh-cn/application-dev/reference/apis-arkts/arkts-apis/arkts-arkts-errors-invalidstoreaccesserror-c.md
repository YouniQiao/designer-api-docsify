# InvalidStoreAccessError

表示发生存储访问错误时抛出的错误。

**继承/实现关系：** InvalidStoreAccessError extends Error

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export class InvalidStoreAccessError--><!--Device-unnamed-export class InvalidStoreAccessError-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

使用指定的错误信息和错误相关信息构造新的InvalidStoreAccessError实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InvalidStoreAccessError-constructor(message?: string, options?: ErrorOptions)--><!--Device-InvalidStoreAccessError-constructor(message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | 错误文本。 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | 错误选项。 |

