# DatePickerResult

日期选择器返回的时间格式。@interface DatePickerResult

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## day

```TypeScript
day?: int
```

选中日期的日。取值范围：与设置的start、end有关，如果没有设置start、end，取值范围为[1, 31]。

**类型：** int

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## month

```TypeScript
month?: int
```

选中日期的月的索引值，索引从0开始，0表示1月，11表示12月。取值范围：与设置的start、end有关，如果没有设置start、end，取值范围为[0, 11]。

**类型：** int

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## year

```TypeScript
year?: int
```

选中日期的年。取值范围：与设置的start、end有关，如果没有设置start、end，取值范围为[1970, 2100]。

**类型：** int

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
