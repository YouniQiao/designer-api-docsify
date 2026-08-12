# on

## on('printerChange')

```TypeScript
function on(type: 'printerChange', callback: PrinterChangeCallback): void
```

注册打印机变动事件回调，使用callback回调。

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

**需要权限：** ohos.permission.PRINT

<!--Device-print-function on(type: 'printerChange', callback: PrinterChangeCallback): void--><!--Device-print-function on(type: 'printerChange', callback: PrinterChangeCallback): void-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'printerChange' | 是 | 表示打印机变动事件。 |
| callback | [PrinterChangeCallback](arkts-basicservices-print-printerchangecallback-t.md) | 是 | 打印机变动之后的回调。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) | the application does not have permission to call this function. |

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

