# AbilityDelegator

AbilityDelegator模块可以通过[AbilityMonitor](arkts-ability-abilitymonitor-i.md#AbilityMonitor)实例来监听和管理 [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md#UIAbility)生命周期的变化。例如获取UIAbility当前状态（如是否已创建/是否在前台等）、查询当前获焦的UIAbility、等待UIAbility进入 某个生命周期节点（如等待UIAbility进入onForeground）、启动指定UIAbility、设置超时机制等功能。 AbilityDelegator可以通过 [getAbilityDelegator](../../apis-test-kit/arkts-apis/arkts-test-abilitydelegatorregistry-getabilitydelegator-f.md#getAbilityDelegator)方 法获取。 > **说明：** > > 本模块接口仅可在[单元测试框架](../../../application-test/unittest-guidelines.md)中使用。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-export interface AbilityDelegator--><!--Device-unnamed-export interface AbilityDelegator-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## addAbilityMonitor

```TypeScript
addAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<void>): void
```

添加AbilityMonitor实例。使用callback异步回调。不支持多线程并发调用。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-addAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<void>): void--><!--Device-AbilityDelegator-addAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 声明AbilityDelegator对象
let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
// 创建AbilityMonitor实例，设置监听的Ability名称和onAbilityCreate生命周期回调
let onAbilityCreateCallback = (data: UIAbility) => {
  console.info(`onAbilityCreateCallback, data: ${JSON.stringify(data)}`);
}

let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

// 获取AbilityDelegator实例
abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
// 调用addAbilityMonitor方法添加监听
abilityDelegator.addAbilityMonitor(monitor, (error: BusinessError) => {
  if (error) {
    console.error(`addAbilityMonitor fail. Code: ${error.code}, message: ${error.message}`);
  }
});
```

## addAbilityMonitor

```TypeScript
addAbilityMonitor(monitor: AbilityMonitor): Promise<void>
```

添加AbilityMonitor实例。使用Promise异步回调。不支持多线程并发调用。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-addAbilityMonitor(monitor: AbilityMonitor): Promise<void>--><!--Device-AbilityDelegator-addAbilityMonitor(monitor: AbilityMonitor): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let onAbilityCreateCallback = (data: UIAbility) => {
  console.info('onAbilityCreateCallback');
};

let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};
let abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();

abilityDelegator.addAbilityMonitor(monitor).then(() => {
  console.info('addAbilityMonitor promise');
});
```

## addAbilityMonitorSync

```TypeScript
addAbilityMonitorSync(monitor: AbilityMonitor): void
```

同步添加AbilityMonitor实例。不支持多线程并发调用。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-addAbilityMonitorSync(monitor: AbilityMonitor): void--><!--Device-AbilityDelegator-addAbilityMonitorSync(monitor: AbilityMonitor): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

let onAbilityCreateCallback = (data: UIAbility) => {
  console.info('onAbilityCreateCallback');
};

let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.addAbilityMonitorSync(monitor);
```

## addAbilityStageMonitor

```TypeScript
addAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<void>): void
```

添加一个AbilityStageMonitor对象，用于监视指定AbilityStage的生命周期状态更改。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-addAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<void>): void--><!--Device-AbilityDelegator-addAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.addAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}, (err: BusinessError) => {
  if (err) {
    console.error(`addAbilityStageMonitor fail. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('addAbilityStageMonitor callback');
  }
});
```

## addAbilityStageMonitor

```TypeScript
addAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>
```

添加一个AbilityStageMonitor对象，用于监视指定AbilityStage的生命周期状态更改。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-addAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>--><!--Device-AbilityDelegator-addAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.addAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}).then(() => {
  console.info('addAbilityStageMonitor promise');
});
```

## addAbilityStageMonitorSync

```TypeScript
addAbilityStageMonitorSync(monitor: AbilityStageMonitor): void
```

同步添加一个AbilityStageMonitor对象，用于监视指定AbilityStage的生命周期状态更改。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-addAbilityStageMonitorSync(monitor: AbilityStageMonitor): void--><!--Device-AbilityDelegator-addAbilityStageMonitorSync(monitor: AbilityStageMonitor): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.addAbilityStageMonitorSync({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
});
```

## addInteropAbilityMonitorSync

```TypeScript
addInteropAbilityMonitorSync(monitor: InteropAbilityMonitor): void
```

新增InteropAbilityMonitor对象，用于监控此进程中指定能力的生命周期状态变化。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-addInteropAbilityMonitorSync(monitor: InteropAbilityMonitor): void--><!--Device-AbilityDelegator-addInteropAbilityMonitorSync(monitor: InteropAbilityMonitor): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [InteropAbilityMonitor](../../apis-test-kit/arkts-apis/arkts-test-abilitydelegatorregistry-interopabilitymonitor-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## doAbilityBackground

```TypeScript
doAbilityBackground(ability: UIAbility, callback: AsyncCallback<void>): void
```

调度指定Ability生命周期状态到Background状态。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-doAbilityBackground(ability: UIAbility, callback: AsyncCallback<void>): void--><!--Device-AbilityDelegator-doAbilityBackground(ability: UIAbility, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  if (err) {
    console.error(`getCurrentTopAbility fail. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('getCurrentTopAbility callback');
    ability = data;
    abilityDelegator.doAbilityBackground(ability, (err: BusinessError) => {
      if (err) {
        console.error(`doAbilityBackground fail. Code: ${err.code}, message: ${err.message}`);
      } else {
        console.info('doAbilityBackground callback');
      }
    });
  }
});
```

## doAbilityBackground

```TypeScript
doAbilityBackground(ability: UIAbility): Promise<void>
```

调度指定Ability生命周期状态到Background状态。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-doAbilityBackground(ability: UIAbility): Promise<void>--><!--Device-AbilityDelegator-doAbilityBackground(ability: UIAbility): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  if (err) {
    console.error(`getCurrentTopAbility fail. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('getCurrentTopAbility callback');
    ability = data;
    abilityDelegator.doAbilityBackground(ability).then(() => {
      console.info('doAbilityBackground promise');
    });
  }
});
```

## doAbilityForeground

```TypeScript
doAbilityForeground(ability: UIAbility, callback: AsyncCallback<void>): void
```

调度指定Ability生命周期状态到Foreground状态。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-doAbilityForeground(ability: UIAbility, callback: AsyncCallback<void>): void--><!--Device-AbilityDelegator-doAbilityForeground(ability: UIAbility, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  if (err) {
    console.error(`getCurrentTopAbility fail. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('getCurrentTopAbility callback');
    ability = data;
    abilityDelegator.doAbilityForeground(ability, (err: BusinessError) => {
      if (err) {
        console.error(`doAbilityForeground fail. Code: ${err.code}, message: ${err.message}`);
      } else {
        console.info('doAbilityForeground callback');
      }
    });
  }
});
```

## doAbilityForeground

```TypeScript
doAbilityForeground(ability: UIAbility): Promise<void>
```

调度指定Ability生命周期状态到Foreground状态。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-doAbilityForeground(ability: UIAbility): Promise<void>--><!--Device-AbilityDelegator-doAbilityForeground(ability: UIAbility): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  if (err) {
    console.error(`getCurrentTopAbility fail. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('getCurrentTopAbility callback');
    ability = data;
    abilityDelegator.doAbilityForeground(ability).then(() => {
      console.info('doAbilityForeground promise');
    });
  }
});
```

## executeShellCommand

```TypeScript
executeShellCommand(cmd: string, callback: AsyncCallback<ShellCmdResult>): void
```

执行指定的shell命令。使用callback异步回调。 仅支持如下shell命令：aa, bm, cp, mkdir, rm, uinput, hilog, ppwd, echo, uitest, acm, hidumper, wukong, pkill, ps, pidof

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-executeShellCommand(cmd: string, callback: AsyncCallback<ShellCmdResult>): void--><!--Device-AbilityDelegator-executeShellCommand(cmd: string, callback: AsyncCallback<ShellCmdResult>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cmd | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ShellCmdResult](arkts-ability-shellcmdresult-shellcmdresult-i.md)&gt; | 是 |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 声明AbilityDelegator对象
let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
// 设置要执行的shell命令字符串
let shellCommand = 'cmd';

// 获取AbilityDelegator实例并执行shell命令
abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.executeShellCommand(shellCommand, (err: BusinessError, data: abilityDelegatorRegistry.ShellCmdResult) => {
  if (err) {
    console.error(`executeShellCommand fail. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('executeShellCommand callback');
  }
});
```

## executeShellCommand

```TypeScript
executeShellCommand(cmd: string, timeoutSecs: number, callback: AsyncCallback<ShellCmdResult>): void
```

指定超时时间，并执行指定的shell命令。使用callback异步回调。 仅支持如下shell命令：aa, bm, cp, mkdir, rm, uinput, hilog, ppwd, echo, uitest, acm, hidumper, wukong, pkill, ps, pidof

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-executeShellCommand(cmd: string, timeoutSecs: long, callback: AsyncCallback<ShellCmdResult>): void--><!--Device-AbilityDelegator-executeShellCommand(cmd: string, timeoutSecs: long, callback: AsyncCallback<ShellCmdResult>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cmd | string | 是 |
| timeoutSecs | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ShellCmdResult](arkts-ability-shellcmdresult-shellcmdresult-i.md)&gt; | 是 |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let shellCommand = 'cmd';
let timeout = 100;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.executeShellCommand(shellCommand, timeout, (err: BusinessError, data: abilityDelegatorRegistry.ShellCmdResult) => {
  if (err) {
    console.error(`executeShellCommand fail. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('executeShellCommand callback');
  }
});
```

## executeShellCommand

```TypeScript
executeShellCommand(cmd: string, timeoutSecs?: number): Promise<ShellCmdResult>
```

指定超时时间，并执行指定的shell命令。使用Promise异步回调。 仅支持如下shell命令：aa, bm, cp, mkdir, rm, uinput, hilog, ppwd, echo, uitest, acm, hidumper, wukong, pkill, ps, pidof

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-executeShellCommand(cmd: string, timeoutSecs?: long): Promise<ShellCmdResult>--><!--Device-AbilityDelegator-executeShellCommand(cmd: string, timeoutSecs?: long): Promise<ShellCmdResult>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cmd | string | 是 |
| timeoutSecs | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ShellCmdResult](arkts-ability-shellcmdresult-shellcmdresult-i.md)&gt; |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let shellCommand = 'cmd';
let timeout = 100;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.executeShellCommand(shellCommand, timeout).then((data) => {
  console.info('executeShellCommand promise');
});
```

## finishTest

```TypeScript
finishTest(msg: string, code: number, callback: AsyncCallback<void>): void
```

结束测试并打印日志信息到单元测试终端控制台。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-finishTest(msg: string, code: long, callback: AsyncCallback<void>): void--><!--Device-AbilityDelegator-finishTest(msg: string, code: long, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| msg | string | 是 |
| code | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let msg = 'msg';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.finishTest(msg, 0, (err: BusinessError) => {
  if (err) {
    console.error(`finishTest fail. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('finishTest callback');
  }
});
```

## finishTest

```TypeScript
finishTest(msg: string, code: number): Promise<void>
```

结束测试并打印日志信息到单元测试终端控制台。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-finishTest(msg: string, code: long): Promise<void>--><!--Device-AbilityDelegator-finishTest(msg: string, code: long): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| msg | string | 是 |
| code | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let msg = 'msg';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.finishTest(msg, 0).then(() => {
  console.info('finishTest promise');
});
```

## getAbilityState

```TypeScript
getAbilityState(ability: UIAbility): number
```

获取指定ability的生命周期状态。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-getAbilityState(ability: UIAbility): int--><!--Device-AbilityDelegator-getAbilityState(ability: UIAbility): int-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  if (err) {
    console.error(`getCurrentTopAbility fail. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('getCurrentTopAbility callback');
    ability = data;
    let state = abilityDelegator.getAbilityState(ability);
    console.info(`getAbilityState ${state}`);
  }
});
```

## getAppContext

```TypeScript
getAppContext(): Context
```

获取应用Context。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-getAppContext(): Context--><!--Device-AbilityDelegator-getAppContext(): Context-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| [Context](arkts-ability-context-c.md) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();

let context = abilityDelegator.getAppContext();
```

## getCurrentTopAbility

```TypeScript
getCurrentTopAbility(callback: AsyncCallback<UIAbility>): void
```

获取当前应用顶部Ability。使用callback异步回调。不支持Worker线程调用。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-getCurrentTopAbility(callback: AsyncCallback<UIAbility>): void--><!--Device-AbilityDelegator-getCurrentTopAbility(callback: AsyncCallback<UIAbility>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  if (err) {
    console.error(`getCurrentTopAbility fail. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('getCurrentTopAbility callback');
    ability = data;
  }
});
```

## getCurrentTopAbility

```TypeScript
getCurrentTopAbility(): Promise<UIAbility>
```

获取当前应用顶部Ability。使用Promise异步回调。不支持Worker线程调用。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-getCurrentTopAbility(): Promise<UIAbility>--><!--Device-AbilityDelegator-getCurrentTopAbility(): Promise<UIAbility>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility().then((data: UIAbility) => {
  console.info('getCurrentTopAbility promise');
  ability = data;
});
```

## print

```TypeScript
print(msg: string, callback: AsyncCallback<void>): void
```

打印日志信息到单元测试终端控制台。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-print(msg: string, callback: AsyncCallback<void>): void--><!--Device-AbilityDelegator-print(msg: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| msg | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let msg = 'msg';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.print(msg, (err: BusinessError) => {
  if (err) {
    console.error(`print fail. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('print callback');
  }
});
```

## print

```TypeScript
print(msg: string): Promise<void>
```

打印日志信息到单元测试终端控制台。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-print(msg: string): Promise<void>--><!--Device-AbilityDelegator-print(msg: string): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| msg | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let msg = 'msg';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.print(msg).then(() => {
  console.info('print promise');
});
```

## printSync

```TypeScript
printSync(msg: string): void
```

打印日志信息到单元测试终端控制台。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-printSync(msg: string): void--><!--Device-AbilityDelegator-printSync(msg: string): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| msg | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let msg = 'msg';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.printSync(msg);
```

## removeAbilityMonitor

```TypeScript
removeAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<void>): void
```

删除已经添加的AbilityMonitor实例。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-removeAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<void>): void--><!--Device-AbilityDelegator-removeAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

let onAbilityCreateCallback = (data: UIAbility) => {
  console.info('onAbilityCreateCallback');
};

let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityMonitor(monitor, (error: BusinessError) => {
  if (error) {
    console.error(`removeAbilityMonitor fail. Code: ${error.code}, message: ${error.message}`);
  }
});
```

## removeAbilityMonitor

```TypeScript
removeAbilityMonitor(monitor: AbilityMonitor): Promise<void>
```

删除已经添加的AbilityMonitor实例。使用Promise异步回调。不支持多线程并发调用。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-removeAbilityMonitor(monitor: AbilityMonitor): Promise<void>--><!--Device-AbilityDelegator-removeAbilityMonitor(monitor: AbilityMonitor): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

let onAbilityCreateCallback = (data: UIAbility) => {
  console.info('onAbilityCreateCallback');
};

let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityMonitor(monitor).then(() => {
  console.info('removeAbilityMonitor promise');
});
```

## removeAbilityMonitorSync

```TypeScript
removeAbilityMonitorSync(monitor: AbilityMonitor): void
```

同步删除已经添加的AbilityMonitor实例。不支持多线程并发调用。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-removeAbilityMonitorSync(monitor: AbilityMonitor): void--><!--Device-AbilityDelegator-removeAbilityMonitorSync(monitor: AbilityMonitor): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

let onAbilityCreateCallback = (data: UIAbility) => {
  console.info('onAbilityCreateCallback');
};

let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityMonitorSync(monitor);
```

## removeAbilityStageMonitor

```TypeScript
removeAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<void>): void
```

从应用程序内存中删除指定的AbilityStageMonitor对象。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-removeAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<void>): void--><!--Device-AbilityDelegator-removeAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}, (err: BusinessError) => {
  if (err) {
    console.error(`removeAbilityStageMonitor fail. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('removeAbilityStageMonitor callback');
  }
});
```

## removeAbilityStageMonitor

```TypeScript
removeAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>
```

从应用程序内存中删除指定的AbilityStageMonitor对象。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-removeAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>--><!--Device-AbilityDelegator-removeAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}).then(() => {
  console.info('removeAbilityStageMonitor promise');
});
```

## removeAbilityStageMonitorSync

```TypeScript
removeAbilityStageMonitorSync(monitor: AbilityStageMonitor): void
```

同步从应用程序内存中删除指定的AbilityStageMonitor对象。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-removeAbilityStageMonitorSync(monitor: AbilityStageMonitor): void--><!--Device-AbilityDelegator-removeAbilityStageMonitorSync(monitor: AbilityStageMonitor): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityStageMonitorSync({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
});
```

## removeInteropAbilityMonitorSync

```TypeScript
removeInteropAbilityMonitorSync(monitor: InteropAbilityMonitor): void
```

从应用程序内存中移除指定的InteropAbilityMonitor对象。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-removeInteropAbilityMonitorSync(monitor: InteropAbilityMonitor): void--><!--Device-AbilityDelegator-removeInteropAbilityMonitorSync(monitor: InteropAbilityMonitor): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [InteropAbilityMonitor](../../apis-test-kit/arkts-apis/arkts-test-abilitydelegatorregistry-interopabilitymonitor-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |

## setMockList

```TypeScript
setMockList(mockList: Record<string, string>): void
```

设置模块的mock替换关系。

**起始版本：** 11

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-setMockList(mockList: Record<string, string>): void--><!--Device-AbilityDelegator-setMockList(mockList: Record<string, string>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mockList | Record & lt;string, string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';

// 创建mock替换关系的键值对象，key为待替换的目标路径，value为mock实现文件路径
let mockList: Record<string, string> = {
  '@ohos.router': 'src/main/mock/ohos/router.mock',
  'common.time': 'src/main/mock/common/time.mock',
};
let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

// 获取AbilityDelegator实例
abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
// 调用setMockList设置mock替换关系
abilityDelegator.setMockList(mockList);
```

## startAbility

```TypeScript
startAbility(want: Want, callback: AsyncCallback<void>): void
```

启动指定Ability。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-startAbility(want: Want, callback: AsyncCallback<void>): void--><!--Device-AbilityDelegator-startAbility(want: Want, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 声明AbilityDelegator对象
let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
// 构造Want参数，指定目标Ability的bundleName和abilityName
let want: Want = {
  bundleName: 'bundleName',
  abilityName: 'abilityName'
};

// 获取AbilityDelegator实例
abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
// 调用startAbility启动指定Ability
abilityDelegator.startAbility(want, (err: BusinessError, data: void) => {
  if (err) {
    console.error(`startAbility fail. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('startAbility callback');
  }
});
```

## startAbility

```TypeScript
startAbility(want: Want): Promise<void>
```

启动指定Ability。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-startAbility(want: Want): Promise<void>--><!--Device-AbilityDelegator-startAbility(want: Want): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { Want } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let want: Want = {
  bundleName: 'bundleName',
  abilityName: 'abilityName'
};

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.startAbility(want).then((data: void) => {
  console.info('startAbility promise');
});
```

## waitAbilityMonitor

```TypeScript
waitAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<UIAbility>): void
```

等待与AbilityMonitor实例匹配的Ability到达OnCreate生命周期，并返回Ability实例。使用callback异步回调。不支持多线程并发调用。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-waitAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<UIAbility>): void--><!--Device-AbilityDelegator-waitAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<UIAbility>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

let onAbilityCreateCallback = (data: UIAbility) => {
  console.info(`onAbilityCreateCallback, data: ${JSON.stringify(data)}`);
}

let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityMonitor(monitor, (error: BusinessError, data: UIAbility) => {
  if (error) {
    console.error(`waitAbilityMonitor fail. Code: ${error.code}, message: ${error.message}`);
  } else {
    console.info('waitAbilityMonitor success.');
  }
});
```

## waitAbilityMonitor

```TypeScript
waitAbilityMonitor(monitor: AbilityMonitor, timeout: number, callback: AsyncCallback<UIAbility>): void
```

设置等待时间，等待与AbilityMonitor实例匹配的Ability到达OnCreate生命周期，并返回Ability实例。使用callback异步回调。不支持多线程并发调用。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-waitAbilityMonitor(monitor: AbilityMonitor, timeout: long, callback: AsyncCallback<UIAbility>): void--><!--Device-AbilityDelegator-waitAbilityMonitor(monitor: AbilityMonitor, timeout: long, callback: AsyncCallback<UIAbility>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | 是 |
| timeout | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 声明AbilityDelegator对象
let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
// 设置最大等待时间（毫秒）
let timeout = 100;
// 创建AbilityMonitor实例，设置监听的Ability名称
let onAbilityCreateCallback = (data: UIAbility) => {
  console.info(`onAbilityCreateCallback, data: ${JSON.stringify(data)}.`);
};

let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

// 获取AbilityDelegator实例
abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
// 调用waitAbilityMonitor并传入超时参数等待匹配Ability
abilityDelegator.waitAbilityMonitor(monitor, timeout, (error: BusinessError, data: UIAbility) => {
  if (error) {
    console.error(`waitAbilityMonitor fail. Code: ${error.code}, message: ${error.message}`);
  } else {
    console.info('waitAbilityMonitor success.');
  }
});
```

## waitAbilityMonitor

```TypeScript
waitAbilityMonitor(monitor: AbilityMonitor, timeout?: number): Promise<UIAbility>
```

设置等待时间，等待与AbilityMonitor实例匹配的Ability到达OnCreate生命周期，并返回Ability实例。使用Promise异步回调。不支持多线程并发调用。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-waitAbilityMonitor(monitor: AbilityMonitor, timeout?: long): Promise<UIAbility>--><!--Device-AbilityDelegator-waitAbilityMonitor(monitor: AbilityMonitor, timeout?: long): Promise<UIAbility>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | 是 |
| timeout | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

let onAbilityCreateCallback = (data: UIAbility) => {
  console.info('onAbilityCreateCallback');
};

let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityMonitor(monitor).then((data: UIAbility) => {
  console.info('waitAbilityMonitor promise');
});
```

## waitAbilityStageMonitor

```TypeScript
waitAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<AbilityStage>): void
```

返回与AbilityStageMonitor中设置条件相匹配的AbilityStage对象。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-waitAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<AbilityStage>): void--><!--Device-AbilityDelegator-waitAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<AbilityStage>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityStage](arkts-ability-app-ability-abilitystage-abilitystage-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { AbilityStage } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}, (err: BusinessError, data: AbilityStage) => {
  if (err) {
    console.error(`waitAbilityStageMonitor fail. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('waitAbilityStageMonitor callback');
  }
});
```

## waitAbilityStageMonitor

```TypeScript
waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout: number, callback: AsyncCallback<AbilityStage>): void
```

在指定的超时最大等待时间内，返回与AbilityStageMonitor中设置条件相匹配的AbilityStage对象。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout: long, callback: AsyncCallback<AbilityStage>): void--><!--Device-AbilityDelegator-waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout: long, callback: AsyncCallback<AbilityStage>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | 是 |
| timeout | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityStage](arkts-ability-app-ability-abilitystage-abilitystage-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { AbilityStage } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let timeout = 100;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}, timeout, (err: BusinessError, data: AbilityStage) => {
  if (err) {
    console.error(`waitAbilityStageMonitor fail. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('waitAbilityStageMonitor callback');
  }
});
```

## waitAbilityStageMonitor

```TypeScript
waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout?: number): Promise<AbilityStage>
```

返回与AbilityStageMonitor中设置条件相匹配的AbilityStage对象，支持设置超时最大等待时间。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-AbilityDelegator-waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout?: long): Promise<AbilityStage>--><!--Device-AbilityDelegator-waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout?: long): Promise<AbilityStage>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | 是 |
| timeout | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AbilityStage](arkts-ability-app-ability-abilitystage-abilitystage-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000100](../errorcode-ability.md#16000100-监听ability生命周期变化的abilitymonitor方法执行失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { AbilityStage } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}).then((data: AbilityStage) => {
  console.info('waitAbilityStageMonitor promise');
});
```
