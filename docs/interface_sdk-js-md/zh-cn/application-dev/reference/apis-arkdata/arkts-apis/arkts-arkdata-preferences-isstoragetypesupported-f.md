# isStorageTypeSupported

## 导入模块

```TypeScript
import { preferences } from 'kits/@kit.ArkData';
```

## isStorageTypeSupported

```TypeScript
function isStorageTypeSupported(type: StorageType): boolean
```

判断当前平台是否支持传入的存储模式，此为同步接口。如果当前平台支持传入的存储模式时，该接口返回true；反之，返回false。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [StorageType](arkts-arkdata-preferences-storagetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
