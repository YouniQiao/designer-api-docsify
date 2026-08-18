# createChecksumSync

## 导入模块

```TypeScript
```

## createChecksumSync

```TypeScript
function createChecksumSync(): Checksum
```

创建校验对象。成功时返回Checksum对象实例。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-zlib-function createChecksumSync(): Checksum--><!--Device-zlib-function createChecksumSync(): Checksum-End-->

**系统能力：** SystemCapability.BundleManager.Zlib

**返回值：**

| 类型 |
| --- |
| [Checksum](arkts-basicservices-zlib-checksum-i.md) |

**示例**

```TypeScript
import { zlib } from '@kit.BasicServicesKit';

let checksum = zlib.createChecksumSync()
```
