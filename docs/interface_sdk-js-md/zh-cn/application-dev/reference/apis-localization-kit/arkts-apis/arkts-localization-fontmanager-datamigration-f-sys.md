# dataMigration（系统接口）

## 导入模块

```TypeScript
import { fontManager } from '@kit.LocalizationKit';
```

## dataMigration

```TypeScript
function dataMigration(callback: DataMigrationCallback): int
```

设备升级时使用的数据迁移接口，用于启动迁移任务，通过回调函数实时反馈迁移进度和结果。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.UPDATE_FONT

**系统能力：** SystemCapability.Global.FontManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [DataMigrationCallback](arkts-localization-fontmanager-datamigrationcallback-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: number<br>ArkTS-Sta：int |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [31100110](../errorcode-font-manager.md#31100110-系统异常导致接口调用失败) |
| [31100111](../errorcode-font-manager.md#31100111-迁移任务执行中) |

**示例**

```TypeScript
import { fontManager } from '@kit.LocalizationKit';

class DataMigrationCallbackImpl implements fontManager.DataMigrationCallback {
  onHeartBeat(): void {
    console.info('onHeartBeat callback');
  }
  onProgress(progress : fontManager.DataMigrationProgress): void {
    console.info('onProgress callback');
  }
  onResult(result : int): void {
    console.info('onResult callback');
  }
}

async function dataMigration() {
  const callback = new DataMigrationCallbackImpl;
  try {
    let res: int = fontManager.dataMigration(callback);
    console.info('dataMigration suc. res is ' + res);
  } catch (error) {
    console.error('dataMigration err.' + error.code);
  }
}
```
