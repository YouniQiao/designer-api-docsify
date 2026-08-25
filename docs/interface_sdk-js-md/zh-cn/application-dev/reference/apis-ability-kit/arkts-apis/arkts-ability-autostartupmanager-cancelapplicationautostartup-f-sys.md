# cancelApplicationAutoStartup（系统接口）

## 导入模块

```TypeScript
import { autoStartupManager } from '@kit.AbilityKit';
```

## cancelApplicationAutoStartup

```TypeScript
function cancelApplicationAutoStartup(info: AutoStartupInfo, callback: AsyncCallback<void>): void
```

取消应用组件开机自启动。使用callback异步回调。 从API version 18开始，该接口仅在2in1和Wearable设备中可正常调用，在其他设备上返回16000050错误码。 对于API version 18之前版本，该接口仅在2in1设备中可正常调用，在其他设备上返回16000050错误码。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_APP_BOOT

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [AutoStartupInfo](arkts-ability-autostartupinfo-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

**示例**

```TypeScript
import { autoStartupManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 取消应用组件开机自启动
  autoStartupManager.cancelApplicationAutoStartup({
    bundleName: 'com.example.autostartupapp',
    abilityName: 'EntryAbility'
  }, (err: BusinessError) => {
    if (err) {
      console.error(`cancelApplicationAutoStartup failed, err code: ${err.code}, msg: ${err.message}.`);
      return;
    }
    console.info(`cancelApplicationAutoStartup success.`);
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let msg = (err as BusinessError).message;
  console.error(`cancelApplicationAutoStartup failed, err code: ${code}, err msg: ${msg}.`);
}
```

```TypeScript
import { autoStartupManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 取消应用组件开机自启动
  autoStartupManager.cancelApplicationAutoStartup({
    bundleName: 'com.example.autostartupapp',
    abilityName: 'EntryAbility'
  }).then(() => {
    console.info(`cancelApplicationAutoStartup success.`);
  }).catch((err: BusinessError) => {
    console.error(`cancelApplicationAutoStartup failed, err code: ${err.code}, msg: ${err.message}.`);
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let msg = (err as BusinessError).message;
  console.error(`cancelApplicationAutoStartup failed, err code: ${code}, err msg: ${msg}.`);
}
```


## cancelApplicationAutoStartup

```TypeScript
function cancelApplicationAutoStartup(info: AutoStartupInfo): Promise<void>
```

取消应用组件开机自启动。使用Promise异步回调。 从API version 18开始，该接口仅在2in1和Wearable设备中可正常调用，在其他设备上返回16000050错误码。 对于API version 18之前版本，该接口仅在2in1设备中可正常调用，在其他设备上返回16000050错误码。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_APP_BOOT

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [AutoStartupInfo](arkts-ability-autostartupinfo-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

**示例**

参见 [cancelApplicationAutoStartup](#cancelapplicationautostartup)
