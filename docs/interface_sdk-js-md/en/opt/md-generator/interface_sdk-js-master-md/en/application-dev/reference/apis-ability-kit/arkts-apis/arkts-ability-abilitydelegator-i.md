# AbilityDelegator

The **AbilityDelegator** module can listen for and manage the lifecycle changes of  
[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md#UIAbility) through  
[AbilityMonitor](./application/AbilityMonitor:AbilityMonitor) instances. For example, you can obtain the current state of a UIAbility (for example, whether the UIAbility has been created or is in the foreground), obtain the UIAbility that currently has the focus, wait for the UIAbility to enter a lifecycle node (for example, the  
**onForeground** state), start a specified UIAbility, and set the timeout mechanism.You can obtain **AbilityDelegator** by calling  
[getAbilityDelegator](../../apis-test-kit/arkts-apis/arkts-test-abilitydelegatorregistry-getabilitydelegator-f.md#getAbilityDelegator).

> **NOTE：**
> 
> The APIs of this module can be used only in [JsUnit](../../../application-test/unittest-guidelines.md).

**Since:** 9

<!--Device-unnamed-export interface AbilityDelegator--><!--Device-unnamed-export interface AbilityDelegator-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## addAbilityMonitor

```TypeScript
addAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<void>): void
```

Adds an **AbilityMonitor** instance. This API uses an asynchronous callback to return the result. Multi-thread concurrent calls are not supported.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-addAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<void>): void--><!--Device-AbilityDelegator-addAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

function onAbilityCreateCallback(data: UIAbility) {
  console.info(`onAbilityCreateCallback, data: ${JSON.stringify(data)}`);
}

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.addAbilityMonitor(monitor, (error: BusinessError) => {
  console.error(`addAbilityMonitor fail, error: ${JSON.stringify(error)}`);
});
```

## addAbilityMonitor

```TypeScript
addAbilityMonitor(monitor: AbilityMonitor): Promise<void>
```

Adds an **AbilityMonitor** instance. This API uses a promise to return the result. Multi-thread concurrent calls are not supported.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-addAbilityMonitor(monitor: AbilityMonitor): Promise<void>--><!--Device-AbilityDelegator-addAbilityMonitor(monitor: AbilityMonitor): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

function onAbilityCreateCallback(data: UIAbility) {
  console.info('onAbilityCreateCallback');
}

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

Adds an **AbilityMonitor** instance. This API returns the result synchronously. Multi-thread concurrent calls are not supported.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-addAbilityMonitorSync(monitor: AbilityMonitor): void--><!--Device-AbilityDelegator-addAbilityMonitorSync(monitor: AbilityMonitor): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

function onAbilityCreateCallback(data: UIAbility) {
  console.info('onAbilityCreateCallback');
}

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

Adds an **AbilityStageMonitor** instance to monitor the lifecycle state changes of an ability stage. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-addAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<void>): void--><!--Device-AbilityDelegator-addAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.addAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}, (err: BusinessError) => {
  console.info('addAbilityStageMonitor callback');
});
```

## addAbilityStageMonitor

```TypeScript
addAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>
```

Adds an **AbilityStageMonitor** instance to monitor the lifecycle state changes of an ability stage. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-addAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>--><!--Device-AbilityDelegator-addAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

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

Adds an **AbilityStageMonitor** instance to monitor the lifecycle state changes of an ability stage. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-addAbilityStageMonitorSync(monitor: AbilityStageMonitor): void--><!--Device-AbilityDelegator-addAbilityStageMonitorSync(monitor: AbilityStageMonitor): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

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

Add an InteropAbilityMonitor object for monitoring the lifecycle state changes of the specified ability  in this process.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AbilityDelegator-addInteropAbilityMonitorSync(monitor: InteropAbilityMonitor): void--><!--Device-AbilityDelegator-addInteropAbilityMonitorSync(monitor: InteropAbilityMonitor): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [InteropAbilityMonitor](arkts-ability-interopabilitymonitor-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |

## doAbilityBackground

```TypeScript
doAbilityBackground(ability: UIAbility, callback: AsyncCallback<void>): void
```

Schedules the lifecycle state of an ability to **Background**. This API uses an asynchronous callback to return the  result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-doAbilityBackground(ability: UIAbility, callback: AsyncCallback<void>): void--><!--Device-AbilityDelegator-doAbilityBackground(ability: UIAbility, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  console.info('getCurrentTopAbility callback');
  ability = data;
  abilityDelegator.doAbilityBackground(ability, (err: BusinessError) => {
    console.info("doAbilityBackground callback");
  });
});
```

## doAbilityBackground

```TypeScript
doAbilityBackground(ability: UIAbility): Promise<void>
```

Schedules the lifecycle state of an ability to **Background**. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-doAbilityBackground(ability: UIAbility): Promise<void>--><!--Device-AbilityDelegator-doAbilityBackground(ability: UIAbility): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  console.info('getCurrentTopAbility callback');
  ability = data;
  abilityDelegator.doAbilityBackground(ability).then(() => {
    console.info("doAbilityBackground promise");
  });
});
```

## doAbilityForeground

```TypeScript
doAbilityForeground(ability: UIAbility, callback: AsyncCallback<void>): void
```

Schedules the lifecycle state of an ability to **Foreground**. This API uses an asynchronous callback to return the  result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-doAbilityForeground(ability: UIAbility, callback: AsyncCallback<void>): void--><!--Device-AbilityDelegator-doAbilityForeground(ability: UIAbility, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  console.info('getCurrentTopAbility callback');
  ability = data;
  abilityDelegator.doAbilityForeground(ability, (err: BusinessError) => {
    console.info("doAbilityForeground callback");
  });
});
```

## doAbilityForeground

```TypeScript
doAbilityForeground(ability: UIAbility): Promise<void>
```

Schedules the lifecycle state of an ability to **Foreground**. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-doAbilityForeground(ability: UIAbility): Promise<void>--><!--Device-AbilityDelegator-doAbilityForeground(ability: UIAbility): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  console.info('getCurrentTopAbility callback');
  ability = data;
  abilityDelegator.doAbilityForeground(ability).then(() => {
    console.info("doAbilityForeground promise");
  });
});
```

## executeShellCommand

```TypeScript
executeShellCommand(cmd: string, callback: AsyncCallback<ShellCmdResult>): void
```

Executes a shell command. This API uses an asynchronous callback to return the result.Only the following shell commands are supported: aa, bm, cp, mkdir, rm, uinput, hilog, ppwd, echo, uitest, acm,hidumper, wukong, pkill, ps, and pidof.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-executeShellCommand(cmd: string, callback: AsyncCallback<ShellCmdResult>): void--><!--Device-AbilityDelegator-executeShellCommand(cmd: string, callback: AsyncCallback<ShellCmdResult>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cmd | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ShellCmdResult](arkts-ability-shellcmdresult-shellcmdresult-i.md)&gt; | Yes |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let cmd = 'cmd';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.executeShellCommand(cmd, (err: BusinessError, data: abilityDelegatorRegistry.ShellCmdResult) => {
  console.info('executeShellCommand callback');
});
```

## executeShellCommand

```TypeScript
executeShellCommand(cmd: string, timeoutSecs: number, callback: AsyncCallback<ShellCmdResult>): void
```

Executes a shell command with the timeout period specified. This API uses an asynchronous callback to return the result.Only the following shell commands are supported: aa, bm, cp, mkdir, rm, uinput, hilog, ppwd, echo, uitest, acm,hidumper, wukong, pkill, ps, and pidof.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-executeShellCommand(cmd: string, timeoutSecs: long, callback: AsyncCallback<ShellCmdResult>): void--><!--Device-AbilityDelegator-executeShellCommand(cmd: string, timeoutSecs: long, callback: AsyncCallback<ShellCmdResult>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cmd | string | Yes |
| timeoutSecs | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ShellCmdResult](arkts-ability-shellcmdresult-shellcmdresult-i.md)&gt; | Yes |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let cmd = 'cmd';
let timeout = 100;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.executeShellCommand(cmd, timeout, (err: BusinessError, data: abilityDelegatorRegistry.ShellCmdResult) => {
  console.info('executeShellCommand callback');
});
```

## executeShellCommand

```TypeScript
executeShellCommand(cmd: string, timeoutSecs?: number): Promise<ShellCmdResult>
```

Executes a shell command with the timeout period specified. This API uses a promise to return the result.Only the following shell commands are supported: aa, bm, cp, mkdir, rm, uinput, hilog, ppwd, echo, uitest, acm,hidumper, wukong, pkill, ps, and pidof.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-executeShellCommand(cmd: string, timeoutSecs?: long): Promise<ShellCmdResult>--><!--Device-AbilityDelegator-executeShellCommand(cmd: string, timeoutSecs?: long): Promise<ShellCmdResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cmd | string | Yes |
| timeoutSecs | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ShellCmdResult](arkts-ability-shellcmdresult-shellcmdresult-i.md)&gt; |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let cmd = 'cmd';
let timeout = 100;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.executeShellCommand(cmd, timeout).then((data) => {
  console.info('executeShellCommand promise');
});
```

## finishTest

```TypeScript
finishTest(msg: string, code: number, callback: AsyncCallback<void>): void
```

Finishes the test and prints log information to the unit test console. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-finishTest(msg: string, code: long, callback: AsyncCallback<void>): void--><!--Device-AbilityDelegator-finishTest(msg: string, code: long, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| msg | string | Yes |
| code | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let msg = 'msg';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.finishTest(msg, 0, (err: BusinessError) => {
  console.info('finishTest callback');
});
```

## finishTest

```TypeScript
finishTest(msg: string, code: number): Promise<void>
```

Finishes the test and prints log information to the unit test console. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-finishTest(msg: string, code: long): Promise<void>--><!--Device-AbilityDelegator-finishTest(msg: string, code: long): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| msg | string | Yes |
| code | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

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

Obtains the lifecycle state of an ability.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-getAbilityState(ability: UIAbility): int--><!--Device-AbilityDelegator-getAbilityState(ability: UIAbility): int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  console.info('getCurrentTopAbility callback');
  ability = data;
  let state = abilityDelegator.getAbilityState(ability);
  console.info(`getAbilityState ${state}`);
});
```

## getAppContext

```TypeScript
getAppContext(): Context
```

Obtains the application context.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-getAppContext(): Context--><!--Device-AbilityDelegator-getAppContext(): Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Context](arkts-ability-context-c.md) |

## Examples

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

Obtains the top ability of this application. This API uses an asynchronous callback to return the result. It cannot  be called in the worker thread.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-getCurrentTopAbility(callback: AsyncCallback<UIAbility>): void--><!--Device-AbilityDelegator-getCurrentTopAbility(callback: AsyncCallback<UIAbility>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  console.info('getCurrentTopAbility callback');
  ability = data;
});
```

## getCurrentTopAbility

```TypeScript
getCurrentTopAbility(): Promise<UIAbility>
```

Obtains the top ability of this application. This API uses a promise to return the result. It cannot be called in the worker thread.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-getCurrentTopAbility(): Promise<UIAbility>--><!--Device-AbilityDelegator-getCurrentTopAbility(): Promise<UIAbility>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |

## Examples

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

Prints log information to the unit test console. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-print(msg: string, callback: AsyncCallback<void>): void--><!--Device-AbilityDelegator-print(msg: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| msg | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let msg = 'msg';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.print(msg, (err: BusinessError) => {
  console.info('print callback');
});
```

## print

```TypeScript
print(msg: string): Promise<void>
```

Prints log information to the unit test console. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-print(msg: string): Promise<void>--><!--Device-AbilityDelegator-print(msg: string): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| msg | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## Examples

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

Prints log information to the unit test console.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-printSync(msg: string): void--><!--Device-AbilityDelegator-printSync(msg: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| msg | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

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

Removes an **AbilityMonitor** instance. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-removeAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<void>): void--><!--Device-AbilityDelegator-removeAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

function onAbilityCreateCallback(data: UIAbility) {
    console.info('onAbilityCreateCallback');
}

let monitor: abilityDelegatorRegistry.AbilityMonitor = {
    abilityName: 'abilityName',
    onAbilityCreate: onAbilityCreateCallback
};

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityMonitor(monitor, (error: BusinessError) => {
    console.error(`removeAbilityMonitor fail, error: ${JSON.stringify(error)}`);
});
```

## removeAbilityMonitor

```TypeScript
removeAbilityMonitor(monitor: AbilityMonitor): Promise<void>
```

Removes an **AbilityMonitor** instance. This API uses a promise to return the result. Multi-thread concurrent calls  are not supported.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-removeAbilityMonitor(monitor: AbilityMonitor): Promise<void>--><!--Device-AbilityDelegator-removeAbilityMonitor(monitor: AbilityMonitor): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

function onAbilityCreateCallback(data: UIAbility) {
  console.info('onAbilityCreateCallback');
}

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityMonitor(monitor).then(() => {
  console.info('removeAbilityMonitor promise');
});
```

## removeAbilityMonitorSync

```TypeScript
removeAbilityMonitorSync(monitor: AbilityMonitor): void
```

Removes an **AbilityMonitor** instance. This API returns the result synchronously. Multi-thread concurrent calls are not supported.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-removeAbilityMonitorSync(monitor: AbilityMonitor): void--><!--Device-AbilityDelegator-removeAbilityMonitorSync(monitor: AbilityMonitor): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

function onAbilityCreateCallback(data: UIAbility) {
  console.info('onAbilityCreateCallback');
}

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityMonitorSync(monitor);
```

## removeAbilityStageMonitor

```TypeScript
removeAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<void>): void
```

Removes an **AbilityStageMonitor** instance from the application memory. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-removeAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<void>): void--><!--Device-AbilityDelegator-removeAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}, (err: BusinessError) => {
  console.info('removeAbilityStageMonitor callback');
});
```

## removeAbilityStageMonitor

```TypeScript
removeAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>
```

Removes an **AbilityStageMonitor** instance from the application memory. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-removeAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>--><!--Device-AbilityDelegator-removeAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

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

Removes an **AbilityStageMonitor** instance from the application memory. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-removeAbilityStageMonitorSync(monitor: AbilityStageMonitor): void--><!--Device-AbilityDelegator-removeAbilityStageMonitorSync(monitor: AbilityStageMonitor): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

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

Remove a specified InteropAbilityMonitor object from the application memory.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AbilityDelegator-removeInteropAbilityMonitorSync(monitor: InteropAbilityMonitor): void--><!--Device-AbilityDelegator-removeInteropAbilityMonitorSync(monitor: InteropAbilityMonitor): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [InteropAbilityMonitor](arkts-ability-interopabilitymonitor-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |

## setMockList

```TypeScript
setMockList(mockList: Record<string, string>): void
```

Sets a list of mock data.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-setMockList(mockList: Record<string, string>): void--><!--Device-AbilityDelegator-setMockList(mockList: Record<string, string>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mockList | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';

let mockList: Record<string, string> = {
  '@ohos.router': 'src/main/mock/ohos/router.mock',
  'common.time': 'src/main/mock/common/time.mock',
};
let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.setMockList(mockList);
```

## startAbility

```TypeScript
startAbility(want: Want, callback: AsyncCallback<void>): void
```

Starts an ability. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-startAbility(want: Want, callback: AsyncCallback<void>): void--><!--Device-AbilityDelegator-startAbility(want: Want, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000053](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000055-installationfree-timeout) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [16000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000002-incorrect-ability-type) |
| [16200001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16200001-caller-released) |
| [16000012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000012-application-under-control) |
| [16000013](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000009](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000010-continuation-flag-is-forbidden) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-context-does-not-exist) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let want: Want = {
  bundleName: 'bundleName',
  abilityName: 'abilityName'
};

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.startAbility(want, (err: BusinessError, data: void) => {
  console.info('startAbility callback');
});
```

## startAbility

```TypeScript
startAbility(want: Want): Promise<void>
```

Starts an ability. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-startAbility(want: Want): Promise<void>--><!--Device-AbilityDelegator-startAbility(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000053](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000055-installationfree-timeout) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [16000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000002-incorrect-ability-type) |
| [16200001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16200001-caller-released) |
| [16000012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000012-application-under-control) |
| [16000013](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000009](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000010-continuation-flag-is-forbidden) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-context-does-not-exist) |

## Examples

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

Waits for the **Ability** instance that matches the **AbilityMonitor** instance to reach the **onCreate** lifecycle  state and returns the **Ability** instance. This API uses an asynchronous callback to return the result. Multi-thread concurrent calls are not supported.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-waitAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<UIAbility>): void--><!--Device-AbilityDelegator-waitAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<UIAbility>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

function onAbilityCreateCallback(data: UIAbility) {
  console.info(`onAbilityCreateCallback, data: ${JSON.stringify(data)}`);
}

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityMonitor(monitor, (error: BusinessError, data: UIAbility) => {
  if (error) {
    console.error(`waitAbilityMonitor fail, error: ${JSON.stringify(error)}`);
  } else {
    console.info(`waitAbilityMonitor success, data: ${JSON.stringify(data)}`);
  }
});
```

## waitAbilityMonitor

```TypeScript
waitAbilityMonitor(monitor: AbilityMonitor, timeout: number, callback: AsyncCallback<UIAbility>): void
```

Waits a period of time for the **Ability** instance that matches the **AbilityMonitor** instance to reach the  
**onCreate** lifecycle state and returns the **Ability** instance. This API uses an asynchronous callback to return  the result. Multi-thread concurrent calls are not supported.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-waitAbilityMonitor(monitor: AbilityMonitor, timeout: long, callback: AsyncCallback<UIAbility>): void--><!--Device-AbilityDelegator-waitAbilityMonitor(monitor: AbilityMonitor, timeout: long, callback: AsyncCallback<UIAbility>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | Yes |
| timeout | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let timeout = 100;
let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

function onAbilityCreateCallback(data: UIAbility) {
  console.info(`onAbilityCreateCallback, data: ${JSON.stringify(data)}.`);
}

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityMonitor(monitor, timeout, (error: BusinessError, data: UIAbility) => {
  if (error && error.code !== 0) {
    console.error(`waitAbilityMonitor fail, error: ${JSON.stringify(error)}`);
  } else {
    console.info(`waitAbilityMonitor success, data: ${JSON.stringify(data)}`);
  }
});
```

## waitAbilityMonitor

```TypeScript
waitAbilityMonitor(monitor: AbilityMonitor, timeout?: number): Promise<UIAbility>
```

Waits a period of time for the **Ability** instance that matches the **AbilityMonitor** instance to reach the  
**onCreate** lifecycle state and returns the **Ability** instance. This API uses a promise to return the result.Multi-thread concurrent calls are not supported.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-waitAbilityMonitor(monitor: AbilityMonitor, timeout?: long): Promise<UIAbility>--><!--Device-AbilityDelegator-waitAbilityMonitor(monitor: AbilityMonitor, timeout?: long): Promise<UIAbility>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [AbilityMonitor](arkts-ability-abilitymonitor-i.md) | Yes |
| timeout | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[UIAbility](arkts-ability-app-ability-uiability-uiability-c.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

function onAbilityCreateCallback(data: UIAbility) {
  console.info('onAbilityCreateCallback');
}

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityMonitor(monitor).then((data: UIAbility) => {
  console.info('waitAbilityMonitor promise');
});
```

## waitAbilityStageMonitor

```TypeScript
waitAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<AbilityStage>): void
```

Returns an **AbilityStage** instance that matches the conditions set in an **AbilityStageMonitor** instance. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-waitAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<AbilityStage>): void--><!--Device-AbilityDelegator-waitAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<AbilityStage>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityStage](arkts-ability-app-ability-abilitystage-abilitystage-c.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

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
  console.info('waitAbilityStageMonitor callback');
});
```

## waitAbilityStageMonitor

```TypeScript
waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout: number, callback: AsyncCallback<AbilityStage>): void
```

Returns an **AbilityStage** instance that matches the conditions set in an **AbilityStageMonitor** instance within the specified timeout period. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout: long, callback: AsyncCallback<AbilityStage>): void--><!--Device-AbilityDelegator-waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout: long, callback: AsyncCallback<AbilityStage>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | Yes |
| timeout | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityStage](arkts-ability-app-ability-abilitystage-abilitystage-c.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

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
  console.info('waitAbilityStageMonitor callback');
});
```

## waitAbilityStageMonitor

```TypeScript
waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout?: number): Promise<AbilityStage>
```

Returns an **AbilityStage** instance that matches the conditions set in an **AbilityStageMonitor** instance. You can specify the timeout period. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityDelegator-waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout?: long): Promise<AbilityStage>--><!--Device-AbilityDelegator-waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout?: long): Promise<AbilityStage>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monitor | [AbilityStageMonitor](arkts-ability-abilitystagemonitor-i.md) | Yes |
| timeout | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AbilityStage](arkts-ability-app-ability-abilitystage-abilitystage-c.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000100-failed-to-call-abilitymonitor-apis-to-listen-for-ability-lifecycle-changes) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

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
