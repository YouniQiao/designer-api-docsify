# DateData

Defines the date data.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare class DateData--><!--Device-unnamed-declare class DateData-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(year: int, month: int, day: int)
```

Constructor of the DateData.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateData-constructor(year: int, month: int, day: int)--><!--Device-DateData-constructor(year: int, month: int, day: int)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| year | int | 是 | set the year of the DateData. |
| month | int | 是 | set the month of the DateData. |
| day | int | 是 | set the day of the DateData. |

## toString

```TypeScript
toString(): string
```

Convert the date data to string.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateData-toString(): string--><!--Device-DateData-toString(): string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | date data in string form. |

## day

```TypeScript
day: int
```

设置日期内联型初始日。 取值范围：[1, 31]。

**类型：** int

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateData-day: int--><!--Device-DateData-day: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## month

```TypeScript
month: int
```

设置日期内联型初始月份。 取值范围：[1, 12]。

**类型：** int

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateData-month: int--><!--Device-DateData-month: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## year

```TypeScript
year: int
```

设置日期内联型初始年份。 取值范围：[1, 5000]。

**类型：** int

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DateData-year: int--><!--Device-DateData-year: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

