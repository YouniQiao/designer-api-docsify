# IDataSource

LazyForEach的数据源，开发者需要实现该接口以提供数据访问和数据变化通知能力，包括获取数据总数、按索引获取数据、注册和注销数据变化监听器等。

**起始版本：** 7

<!--Device-unnamed-declare interface IDataSource--><!--Device-unnamed-declare interface IDataSource-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## getData

```TypeScript
getData(index: number): any
```

获取索引值index对应的数据。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-IDataSource-getData(index: number): any--><!--Device-IDataSource-getData(index: number): any-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| any |

## registerDataChangeListener

```TypeScript
registerDataChangeListener(listener: DataChangeListener): void
```

注册数据改变的监听器。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-IDataSource-registerDataChangeListener(listener: DataChangeListener): void--><!--Device-IDataSource-registerDataChangeListener(listener: DataChangeListener): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| listener | [DataChangeListener](arkts-arkui-datachangelistener-i.md) | 是 |

## totalCount

```TypeScript
totalCount(): number
```

获得数据总数。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-IDataSource-totalCount(): number--><!--Device-IDataSource-totalCount(): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## unregisterDataChangeListener

```TypeScript
unregisterDataChangeListener(listener: DataChangeListener): void
```

注销数据改变的监听器。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-IDataSource-unregisterDataChangeListener(listener: DataChangeListener): void--><!--Device-IDataSource-unregisterDataChangeListener(listener: DataChangeListener): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| listener | [DataChangeListener](arkts-arkui-datachangelistener-i.md) | 是 |
