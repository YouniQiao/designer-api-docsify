# PrinterInfoQueryCallback（系统接口）

```TypeScript
type PrinterInfoQueryCallback = (printerInfo: PrinterInformation, ppdInfo: PpdInfo[]) => void
```

定义注册监听printInfoQuery事件的回调类型。 printInfo的值表示打印机信息。 ppdInfo的值表示所有打印机的ppd信息。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| printerInfo | [PrinterInformation](arkts-basicservices-print-printerinformation-i.md) | 是 |
| ppdInfo | [PpdInfo](arkts-basicservices-print-ppdinfo-i.md)[] | 是 |
