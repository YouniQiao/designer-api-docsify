# installPrivateCertificate

## 导入模块

```TypeScript
```

## installPrivateCertificate

```TypeScript
function installPrivateCertificate(
    keystore: Uint8Array,
    keystorePwd: string,
    certAlias: string,
    callback: AsyncCallback<CMResult>
  ): void
```

安装私有凭据。使用Callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

<!--Device-certificateManager-function installPrivateCertificate(    keystore: Uint8Array,    keystorePwd: string,    certAlias: string,    callback: AsyncCallback<CMResult>  ): void--><!--Device-certificateManager-function installPrivateCertificate(    keystore: Uint8Array,    keystorePwd: string,    certAlias: string,    callback: AsyncCallback<CMResult>  ): void-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keystore | Uint8Array | 是 |
| keystorePwd | string | 是 |
| certAlias | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17500003](../errorcode-certManager.md#17500003-证书或凭据无效) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17500001](../errorcode-certManager.md#17500001-内部错误) |
| [17500004](../errorcode-certManager.md#17500004-证书或凭据数量达到上限) |

**示例**

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';

/* 安装的凭据数据需要业务赋值，本例数据非凭据数据 */
let keystore: Uint8Array = new Uint8Array([
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01
]);
let keystorePwd: string = '123456';
try {
  certificateManager.installPrivateCertificate(keystore, keystorePwd, 'test', (err, cmResult) => {
    if (err != null) {
      console.error(`Failed to install private certificate. Code: ${err.code}, message: ${err.message}`);
    } else {
      let uri: string = cmResult?.uri ?? '';
      console.info('Succeeded in installing private certificate.');
    }
  });
} catch (error) {
  console.error(`Failed to install private certificate. Code: ${error.code}, message: ${error.message}`);
}
```


## installPrivateCertificate

```TypeScript
function installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string): Promise<CMResult>
```

安装私有凭据。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

<!--Device-certificateManager-function installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string): Promise<CMResult>--><!--Device-certificateManager-function installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string): Promise<CMResult>-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keystore | Uint8Array | 是 |
| keystorePwd | string | 是 |
| certAlias | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17500003](../errorcode-certManager.md#17500003-证书或凭据无效) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17500001](../errorcode-certManager.md#17500001-内部错误) |
| [17500004](../errorcode-certManager.md#17500004-证书或凭据数量达到上限) |

**示例**

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* 安装的凭据数据需要业务赋值，本例数据非凭据数据 */
let keystore: Uint8Array = new Uint8Array([
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01
]);
let keystorePwd: string = '123456';
try {
  certificateManager.installPrivateCertificate(keystore, keystorePwd, 'test').then((cmResult) => {
    let uri: string = cmResult?.uri ?? '';
    console.info('Succeeded in installing private certificate.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to install private certificate. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to install private certificate. Code: ${error.code}, message: ${error.message}`);
}
```


## installPrivateCertificate

```TypeScript
function installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string, level: AuthStorageLevel): Promise<CMResult>
```

表示安装私有凭据并指定凭据的存储级别。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.ACCESS_CERT_MANAGER

<!--Device-certificateManager-function installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string, level: AuthStorageLevel): Promise<CMResult>--><!--Device-certificateManager-function installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string, level: AuthStorageLevel): Promise<CMResult>-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keystore | Uint8Array | 是 |
| keystorePwd | string | 是 |
| certAlias | string | 是 |
| level | [AuthStorageLevel](arkts-devicecertificate-certificatemanager-authstoragelevel-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17500003](../errorcode-certManager.md#17500003-证书或凭据无效) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17500001](../errorcode-certManager.md#17500001-内部错误) |
| [17500004](../errorcode-certManager.md#17500004-证书或凭据数量达到上限) |

**示例**

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* 安装的凭据数据需要业务赋值，本例数据非凭据数据。 */
let keystore: Uint8Array = new Uint8Array([
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01
]);
let keystorePwd: string = '123456';
try {
  /* 安装凭据在首次解锁设备后可以使用。 */
  let level = certificateManager.AuthStorageLevel.EL2;
  certificateManager.installPrivateCertificate(keystore, keystorePwd, 'test', level).then((cmResult) => {
    let uri: string = cmResult.uri ?? '';
    console.info('Succeeded in installing private certificate.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to install private certificate. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to install private certificate. Code: ${error.code}, message: ${error.message}`);
}
```
