# off（系统接口）

## off('appForegroundState')

```TypeScript
function off(type: 'appForegroundState', observer?: AppForegroundStateObserver): void
```

注销应用启动和退出的监听器。

**起始版本：** 11

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function off(type: 'appForegroundState', observer?: AppForegroundStateObserver): void--><!--Device-appManager-function off(type: 'appForegroundState', observer?: AppForegroundStateObserver): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'appForegroundState' | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [AppForegroundStateObserver](arkts-ability-appforegroundstateobserver-i-sys.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let savedObserver: appManager.AppForegroundStateObserver | undefined;
// 1.注册应用启动和退出的监听器
let observer: appManager.AppForegroundStateObserver = {
  onAppStateChanged(appStateData: appManager.AppStateData) {
    console.info(`[appManager] onAppStateChanged: ${JSON.stringify(appStateData)}`);
  },
};

try {
  appManager.on('appForegroundState', observer);
  // 保存observer对象，用于注销
  savedObserver = observer;
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}

// 2.注销监听器
try {
  appManager.off('appForegroundState',  savedObserver);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```


## off('abilityFirstFrameState')

```TypeScript
function off(type: 'abilityFirstFrameState', observer?: AbilityFirstFrameStateObserver): void
```

取消注册监听Ability首帧绘制完成事件观察者对象。

**起始版本：** 12

**需要权限：** ohos.permission.RUNNING_STATE_OBSERVER

<!--Device-appManager-function off(type: 'abilityFirstFrameState', observer?: AbilityFirstFrameStateObserver): void--><!--Device-appManager-function off(type: 'abilityFirstFrameState', observer?: AbilityFirstFrameStateObserver): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'abilityFirstFrameState' | 是 |
| [observer](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer.md) | [AbilityFirstFrameStateObserver](arkts-ability-appmanager-abilityfirstframestateobserver-t-sys.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityFirstFrameStateObserverForAll: appManager.AbilityFirstFrameStateObserver = {
  onAbilityFirstFrameDrawn(abilityStateData: appManager.AbilityFirstFrameStateData) {
    console.info('abilityFirstFrame: ', JSON.stringify(abilityStateData));
  }
};

try {
  appManager.on('abilityFirstFrameState', abilityFirstFrameStateObserverForAll);
} catch (e) {
  let code = (e as BusinessError).code;
  let message = (e as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}

try {
  appManager.off('abilityFirstFrameState', abilityFirstFrameStateObserverForAll);
} catch (e) {
  let code = (e as BusinessError).code;
  let message = (e as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```
