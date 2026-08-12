# off（系统接口）

## off('abilityForegroundState')

```TypeScript
function off(type: 'abilityForegroundState', observer?: AbilityForegroundStateObserver): void
```

取消注册Ability启动和退出的观测器。

**起始版本：** 11

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-abilityManager-function off(type: 'abilityForegroundState', observer?: AbilityForegroundStateObserver): void--><!--Device-abilityManager-function off(type: 'abilityForegroundState', observer?: AbilityForegroundStateObserver): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'abilityForegroundState' | 是 |
| observer | [AbilityForegroundStateObserver](arkts-ability-abilitymanager-abilityforegroundstateobserver-t-sys.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observer_: abilityManager.AbilityForegroundStateObserver | undefined;
// 1.注册应用启动和退出的监听器
let observer: abilityManager.AbilityForegroundStateObserver = {
  onAbilityStateChanged(abilityStateData: abilityManager.AbilityStateData) {
    console.info(`onAbilityStateChanged: ${JSON.stringify(abilityStateData)}`);
  },
};
try {
  abilityManager.on('abilityForegroundState', observer);
  observer_ = observer;
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message} `);
}

// 2.注销监听器
try {
  abilityManager.off('abilityForegroundState',  observer_);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message} `);
}
```
