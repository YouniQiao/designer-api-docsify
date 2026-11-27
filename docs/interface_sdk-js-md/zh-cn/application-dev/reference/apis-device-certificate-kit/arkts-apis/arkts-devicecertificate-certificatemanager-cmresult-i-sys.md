# CMResult（系统接口）

```TypeScript
export interface CMResult
```

表示接口的返回结果。

**起始版本：** 11

<!--Device-certificateManager-export interface CMResult--><!--Device-certificateManager-export interface CMResult-End-->

**系统能力：** SystemCapability.Security.CertificateManager

## 导入模块

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
```

## certStoreInfo

```TypeScript
certStoreInfo?: CertStoreInfo
```

证书库信息。

**类型：** [CertStoreInfo](arkts-devicecertificate-certificatemanager-certstoreinfo-i-sys.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CMResult-certStoreInfo?: CertStoreInfo--><!--Device-CMResult-certStoreInfo?: CertStoreInfo-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**系统接口：** 此接口为系统接口。
