# CertStoreInfo（系统接口）

```TypeScript
export interface CertStoreInfo
```

表示证书库信息。

**起始版本：** 26.1.0

<!--Device-certificateManager-export interface CertStoreInfo--><!--Device-certificateManager-export interface CertStoreInfo-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
```

## certStoreVersion

```TypeScript
certStoreVersion: string
```

国际算法系统证书库的版本号。

**类型：** string

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CertStoreInfo-certStoreVersion: string--><!--Device-CertStoreInfo-certStoreVersion: string-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**系统接口：** 此接口为系统接口。

## smCertStoreVersion

```TypeScript
smCertStoreVersion?: string
```

国密算法系统证书库的版本号。

**类型：** string

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CertStoreInfo-smCertStoreVersion?: string--><!--Device-CertStoreInfo-smCertStoreVersion?: string-End-->

**系统能力：** SystemCapability.Security.CertificateManager

**系统接口：** 此接口为系统接口。
