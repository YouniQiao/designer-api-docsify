# ZoneOffsetTransition

提供解析时区跳变规则的能力。

**起始版本：** 23

<!--Device-i18n-export class ZoneOffsetTransition--><!--Device-i18n-export class ZoneOffsetTransition-End-->

**系统能力：** SystemCapability.Global.I18n

## 导入模块

```TypeScript
```

## getMilliseconds

```TypeScript
public getMilliseconds(): number
```

获取时区跳变点的时间戳。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-ZoneOffsetTransition-public getMilliseconds(): double--><!--Device-ZoneOffsetTransition-public getMilliseconds(): double-End-->

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| number |

## getOffsetAfter

```TypeScript
public getOffsetAfter(): number
```

获取时区跳变后的偏移量。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-ZoneOffsetTransition-public getOffsetAfter(): int--><!--Device-ZoneOffsetTransition-public getOffsetAfter(): int-End-->

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| number |

## getOffsetBefore

```TypeScript
public getOffsetBefore(): number
```

获取时区跳变前的偏移量。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-ZoneOffsetTransition-public getOffsetBefore(): int--><!--Device-ZoneOffsetTransition-public getOffsetBefore(): int-End-->

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| number |
