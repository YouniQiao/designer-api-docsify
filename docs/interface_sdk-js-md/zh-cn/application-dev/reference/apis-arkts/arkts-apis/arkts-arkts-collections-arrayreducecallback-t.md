# ArrayReduceCallback

```TypeScript
type ArrayReduceCallback<AccType, ElementType, ArrayType> =
    (previousValue: AccType, currentValue: ElementType, currentIndex: number, array: ArrayType) => AccType
```

ArkTS Array归约函数类型，被Array类的'reduceRight'接口使用。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| previousValue | AccType | 是 |
| [currentValue](../../apis-notification-kit/arkts-apis/arkts-notification-notificationcontent-notificationprogress-i.md) | ElementType | 是 |
| currentIndex | number | 是 |
| array | ArrayType | 是 |

**返回值：**

| 类型 |
| --- |
| AccType |
