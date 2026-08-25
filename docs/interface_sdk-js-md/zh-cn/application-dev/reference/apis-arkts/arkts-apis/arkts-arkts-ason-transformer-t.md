# Transformer

```TypeScript
type Transformer = (this: ISendable, key: string,
      value: ISendable | undefined | null) => ISendable | undefined | null
```

用于转换结果函数的类型。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| this | [ISendable](../../apis-image-kit/arkts-apis/arkts-image-sendableimage-isendable-t.md) | 是 |
| key | string | 是 |
| value | ISendable \| undefined \| null | 是 |

**返回值：**

| 类型 |
| --- |
| ISendable \| undefined \| null |
