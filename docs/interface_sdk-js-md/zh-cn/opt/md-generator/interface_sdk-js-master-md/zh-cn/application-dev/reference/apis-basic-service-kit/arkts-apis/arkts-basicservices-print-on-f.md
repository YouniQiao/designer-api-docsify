# on

## on('printerChange')

```TypeScript
function on(type: 'printerChange', callback: PrinterChangeCallback): void
```

注册打印机变动事件回调，使用callback回调。

**起始版本：** 18

**需要权限：** ohos.permission.PRINT

<!--Device-print-function on(type: 'printerChange', callback: PrinterChangeCallback): void--><!--Device-print-function on(type: 'printerChange', callback: PrinterChangeCallback): void-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'printerChange' | 是 |
| callback | [PrinterChangeCallback](arkts-basicservices-print-printerchangecallback-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { print } from '@kit.BasicServicesKit';

// Trigger this callback when a added printer is changed.
let onPrinterChange =
    (event: print.PrinterEvent, printerInformation: print.PrinterInformation) => {
        console.info('printerChange, event: ' + event + ', printerInformation: ' + JSON.stringify(printerInformation));
    };
print.on('printerChange', onPrinterChange);
```
