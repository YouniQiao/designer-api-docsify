# getPrinterInfoById（系统接口）

## getPrinterInfoById

```TypeScript
function getPrinterInfoById(printerId: string): Promise<PrinterInfo>
```

根据打印机id获取打印机信息，使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

<!--Device-print-function getPrinterInfoById(printerId: string): Promise<PrinterInfo>--><!--Device-print-function getPrinterInfoById(printerId: string): Promise<PrinterInfo>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| printerId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PrinterInfo](arkts-basicservices-print-printerinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerId : string = '1';
print.getPrinterInfoById(printerId).then((printerInfo : print.PrinterInfo) => {
    console.info('getPrinterInfoById data : ' + JSON.stringify(printerInfo));
}).catch((error: BusinessError) => {
    console.error(`Failed to get printer info by id. Code: ${error.code}, message: ${error.message}`);
});
```
