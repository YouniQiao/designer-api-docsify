# JsonTypeError

以不兼容的类型访问JSON元素时抛出的错误。 例如，尝试从number类型的元素中获取字符串值。

**继承/实现关系：** JsonTypeError extends [JsonError](arkts-arkts-jsonx-jsonerror-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-jsonx-export class JsonTypeError--><!--Device-jsonx-export class JsonTypeError-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
public constructor(msg: string)
```

使用指定的错误信息构造新的JsonTypeError。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonTypeError-public constructor(msg: string)--><!--Device-JsonTypeError-public constructor(msg: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msg | string | 是 | 错误信息。 |

