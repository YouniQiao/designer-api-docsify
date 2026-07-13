# ZoneRules

提供查询时区跳变规则的能力。

**起始版本：** 20

**系统能力：** SystemCapability.Global.I18n

## nextTransition

```TypeScript
public nextTransition(date?: number): ZoneOffsetTransition
```

获取指定时间的下一个时区跳变对象。

**起始版本：** 20

**元服务API：** 从API版本20开始，该接口支持在元服务API中使用。

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| date | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ZoneOffsetTransition | 时区跳变对象。 |

