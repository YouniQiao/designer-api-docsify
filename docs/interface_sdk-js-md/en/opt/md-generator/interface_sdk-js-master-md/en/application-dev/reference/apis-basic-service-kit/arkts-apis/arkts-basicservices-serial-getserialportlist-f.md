# getSerialPortList

## Modules to Import

```TypeScript
import { serial } from '@kit.BasicServicesKit';
```

## getSerialPortList

```TypeScript
function getSerialPortList(): Promise<SerialPort[]>
```

Obtains the serial port list. This API returns the result asynchronously through a promise.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-serial-function getSerialPortList(): Promise<SerialPort[]>--><!--Device-serial-function getSerialPortList(): Promise<SerialPort[]>-End-->

**System capability:** SystemCapability.BusManager.Serial

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;SerialPort[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35700001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-busmanager-serial.md#35700001-abnormal-service) |
| [203](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
