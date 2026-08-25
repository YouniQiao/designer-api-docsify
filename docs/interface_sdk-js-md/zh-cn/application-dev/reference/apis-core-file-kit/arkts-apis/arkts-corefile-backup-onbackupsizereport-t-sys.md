# OnBackupSizeReport（系统接口）

```TypeScript
type OnBackupSizeReport = (reportInfo: string) => void
```

返回应用备份数据量信息的回调函数。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.StorageService.Backup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reportInfo | string | 是 |

**示例**

```TypeScript
import { backup } from '@kit.CoreFileKit';

onBackupSizeReport: (OnBackupSizeReport: backup.OnBackupSizeReport) => {
  console.info('dataSizeCallback success');
  console.info('dataSizeCallback report : ' + OnBackupSizeReport);
}
```
