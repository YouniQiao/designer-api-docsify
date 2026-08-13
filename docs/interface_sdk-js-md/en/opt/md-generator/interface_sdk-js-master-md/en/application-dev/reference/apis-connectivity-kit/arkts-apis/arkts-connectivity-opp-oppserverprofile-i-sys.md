# OppServerProfile

Manager OPP server profile.

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-opp-interface OppServerProfile--><!--Device-opp-interface OppServerProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { opp } from '@kit.ConnectivityKit';
```

## cancelTransfer

```TypeScript
cancelTransfer(): Promise<void>
```

cancel the current file transfer action.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppServerProfile-cancelTransfer(): Promise<void>--><!--Device-OppServerProfile-cancelTransfer(): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2903002 |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
| 2900001 |
| 2900003 |
| 2900099 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { opp } from '@kit.ConnectivityKit';
// Create fileHolders.
try {
    let oppProfile = opp.createOppServerProfile();
    oppProfile.cancelTransfer();
} catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## getCurrentTransferInformation

```TypeScript
getCurrentTransferInformation(): Promise<OppTransferInformation>
```

Obtains the information about the file that is being transferred. On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** 
- API version 26.0.0+: ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC)
- API version 16 - 24: ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppServerProfile-getCurrentTransferInformation(): Promise<OppTransferInformation>--><!--Device-OppServerProfile-getCurrentTransferInformation(): Promise<OppTransferInformation>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OppTransferInformation](arkts-connectivity-opp-opptransferinformation-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 2903004 |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
| 2900001 |
| 2900003 |
| 2900099 |

## offReceiveIncomingFile

```TypeScript
offReceiveIncomingFile(callback?: Callback<OppTransferInformation>): void
```

Unsubscribe to the event of receiving a file transfer request.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppServerProfile-offReceiveIncomingFile(callback?: Callback<OppTransferInformation>): void--><!--Device-OppServerProfile-offReceiveIncomingFile(callback?: Callback<OppTransferInformation>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OppTransferInformation](arkts-connectivity-opp-opptransferinformation-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
| 2900001 |
| 2900003 |

## offTransferStateChange

```TypeScript
offTransferStateChange(callback?: Callback<OppTransferInformation>): void
```

Unsubscribe the event reported when the file transfer status changes.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppServerProfile-offTransferStateChange(callback?: Callback<OppTransferInformation>): void--><!--Device-OppServerProfile-offTransferStateChange(callback?: Callback<OppTransferInformation>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OppTransferInformation](arkts-connectivity-opp-opptransferinformation-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
| 2900001 |
| 2900003 |

## off_receiveIncomingFile

```TypeScript
off(type: 'receiveIncomingFile', callback?: Callback<OppTransferInformation>): void
```

Unsubscribe to the event of receiving a file transfer request.

**Since:** 16

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppServerProfile-off(type: 'receiveIncomingFile', callback?: Callback<OppTransferInformation>): void--><!--Device-OppServerProfile-off(type: 'receiveIncomingFile', callback?: Callback<OppTransferInformation>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'receiveIncomingFile' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OppTransferInformation](arkts-connectivity-opp-opptransferinformation-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
| 2900001 |
| 2900003 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { opp } from '@kit.ConnectivityKit';
// Create fileHolders.
try {
    let oppProfile = opp.createOppServerProfile();
    oppProfile.off("receiveIncomingFile");
} catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## off_transferStateChange

```TypeScript
off(type: 'transferStateChange', callback?: Callback<OppTransferInformation>): void
```

Unsubscribe the event reported when the file transfer status changes.

**Since:** 16

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppServerProfile-off(type: 'transferStateChange', callback?: Callback<OppTransferInformation>): void--><!--Device-OppServerProfile-off(type: 'transferStateChange', callback?: Callback<OppTransferInformation>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'transferStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OppTransferInformation](arkts-connectivity-opp-opptransferinformation-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
| 2900001 |
| 2900003 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { opp } from '@kit.ConnectivityKit';
// Create fileHolders.
try {
    let oppProfile = opp.createOppServerProfile();
    oppProfile.off("transferStateChange");
} catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## onReceiveIncomingFile

```TypeScript
onReceiveIncomingFile(callback: Callback<OppTransferInformation>): void
```

Subscribe to the event of receiving a file transfer request. If the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC)

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppServerProfile-onReceiveIncomingFile(callback: Callback<OppTransferInformation>): void--><!--Device-OppServerProfile-onReceiveIncomingFile(callback: Callback<OppTransferInformation>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OppTransferInformation](arkts-connectivity-opp-opptransferinformation-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
| 2900001 |
| 2900003 |

## onTransferStateChange

```TypeScript
onTransferStateChange(callback: Callback<OppTransferInformation>): void
```

Subscribe the event reported when the file transfer status changes. If the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC)

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppServerProfile-onTransferStateChange(callback: Callback<OppTransferInformation>): void--><!--Device-OppServerProfile-onTransferStateChange(callback: Callback<OppTransferInformation>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OppTransferInformation](arkts-connectivity-opp-opptransferinformation-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
| 2900001 |
| 2900003 |

## on_receiveIncomingFile

```TypeScript
on(type: 'receiveIncomingFile', callback: Callback<OppTransferInformation>): void
```

Subscribe to the event of receiving a file transfer request. On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual.

**Since:** 16

**Deprecated since:** -1

**Required permissions:** 
- API version 26.0.0+: ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC)
- API version 16 - 24: ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppServerProfile-on(type: 'receiveIncomingFile', callback: Callback<OppTransferInformation>): void--><!--Device-OppServerProfile-on(type: 'receiveIncomingFile', callback: Callback<OppTransferInformation>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'receiveIncomingFile' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OppTransferInformation](arkts-connectivity-opp-opptransferinformation-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
| 2900001 |
| 2900003 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { opp } from '@kit.ConnectivityKit';
// Create fileHolders.
try {
    let oppProfile = opp.createOppServerProfile();
    oppProfile.on("receiveIncomingFile", (data: opp.OppTransferInformation) => {
        if (data.status == opp.TransferStatus.PENDING) {
          console.info("[opp_js] received file waiting to confirm : " + data.remoteDeviceName);
        } else if (data.status == opp.TransferStatus.RUNNING){
          console.info("[opp_js] running data.currentBytes " + data.currentBytes + " data.totalBytes" + data.totalBytes);
        } else if (data.status == opp.TransferStatus.FINISH){
          console.info("[opp_js] transfer finished, result is " + data.result);
        }
      });
} catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## on_transferStateChange

```TypeScript
on(type: 'transferStateChange', callback: Callback<OppTransferInformation>): void
```

Subscribe the event reported when the file transfer status changes. On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual.

**Since:** 16

**Deprecated since:** -1

**Required permissions:** 
- API version 26.0.0+: ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC)
- API version 16 - 24: ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppServerProfile-on(type: 'transferStateChange', callback: Callback<OppTransferInformation>): void--><!--Device-OppServerProfile-on(type: 'transferStateChange', callback: Callback<OppTransferInformation>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'transferStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OppTransferInformation](arkts-connectivity-opp-opptransferinformation-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
| 2900001 |
| 2900003 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { opp } from '@kit.ConnectivityKit';
// Create fileHolders.
try {
    let oppProfile = opp.createOppServerProfile();
    oppProfile.on("transferStateChange", (data: opp.OppTransferInformation) => {
        if (data.status == opp.TransferStatus.PENDING) {
          console.info("[opp_js] waiting to transfer : " + data.remoteDeviceName);
        } else if (data.status == opp.TransferStatus.RUNNING){
          console.info("[opp_js] running data.currentBytes " + data.currentBytes + " data.totalBytes" + data.totalBytes);
        } else if (data.status == opp.TransferStatus.FINISH){
          console.info("[opp_js] transfer finished, result is " + data.result);
        }
      });
} catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## sendFile

```TypeScript
sendFile(deviceId: string, fileHolds: Array<FileHolder>): Promise<void>
```

Send files to the remote device.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppServerProfile-sendFile(deviceId: string, fileHolds: Array<FileHolder>): Promise<void>--><!--Device-OppServerProfile-sendFile(deviceId: string, fileHolds: Array<FileHolder>): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| fileHolds | Array&lt;[FileHolder](arkts-connectivity-opp-fileholder-i-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2903001 |
| 2903002 |
| 2903003 |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
| 2900001 |
| 2900003 |
| 2900099 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs} from '@kit.CoreFileKit';
import { opp } from '@kit.ConnectivityKit';
// Create fileHolders.
try {
    let oppProfile = opp.createOppServerProfile();
    let fileHolders : Array<opp.FileHolder> = [];
    // Valid URIs
    let uris: Array<string> = ['test1.jpg', 'test2.jpg'];
    for (let i = 0; i < uris.length; i++) {
        let filePath = uris[i];
        console.info('opp deal filePath is :' + filePath);
        let file = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
        let stat: fs.Stat = fs.statSync(file.fd);
        let fileHolder: opp.FileHolder = {
        filePath:filePath,
        fileSize:stat.size,
        fileFd:file.fd
        };
        fileHolders.push(fileHolder);
    }
    oppProfile.sendFile("11:22:33:44:55:66", fileHolders);
    // After the file transfer is complete, call fs.close(file.fd) to close the file descriptor.
} catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## setIncomingFileConfirmation

```TypeScript
setIncomingFileConfirmation(accept: boolean, fileFd: number): Promise<void>
```

Set the user confirmation information for incoming files.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppServerProfile-setIncomingFileConfirmation(accept: boolean, fileFd: int): Promise<void>--><!--Device-OppServerProfile-setIncomingFileConfirmation(accept: boolean, fileFd: int): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accept | boolean | Yes |
| [fileFd](arkts-connectivity-opp-fileholder-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2903002 |
| 2903003 |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
| 2900001 |
| 2900003 |
| 2900099 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs} from '@kit.CoreFileKit';
import { opp } from '@kit.ConnectivityKit';
// Create fileHolders.
let file: fs.File | undefined = undefined;
try {
    let oppProfile = opp.createOppServerProfile();
    let pathDir = "/test.jpg"; // Replace the example path with the actual one.
    file = fs.openSync(pathDir, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
    oppProfile.setIncomingFileConfirmation(true, file.fd);
} catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
} finally {
  // Close the file descriptor after file receiving is complete. 
  if (file) {
    fs.close(file.fd);
  }
}
```

## setLastReceivedFileUri

```TypeScript
setLastReceivedFileUri(uri: string): Promise<void>
```

Set the URI of the last received file.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-OppServerProfile-setLastReceivedFileUri(uri: string): Promise<void>--><!--Device-OppServerProfile-setLastReceivedFileUri(uri: string): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900004 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
| 2900001 |
| 2900003 |
| 2900099 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { opp } from '@kit.ConnectivityKit';
// Create fileHolders.
try {
    let oppProfile = opp.createOppServerProfile();
    oppProfile.setLastReceivedFileUri("file://media/Photo/1/IMG_1739266559_000/screenshot_20250211_173419.jpg"); // Replace the example path with the actual one.
} catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
