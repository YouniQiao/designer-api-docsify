# disconnectAbility

## Modules to Import

```TypeScript
import { particleAbility } from '@kit.AbilityKit';
```

## disconnectAbility

```TypeScript
function disconnectAbility(connection: number, callback: AsyncCallback<void>): void
```

Disconnects this ability from a specific ServiceAbility. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-particleAbility-function disconnectAbility(connection: number, callback: AsyncCallback<void>): void--><!--Device-particleAbility-function disconnectAbility(connection: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| connection | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { particleAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

let connId = particleAbility.connectAbility(
  {
    bundleName: 'com.ix.ServiceAbility',
    abilityName: 'ServiceAbilityA',
  },
  {
    onConnect: (element, remote) => {
      console.info(`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}`);
    },
    onDisconnect: (element) => {
      console.info(`ConnectAbility onDisconnect element.deviceId: ${element.deviceId}`);
    },
    onFailed: (code) => {
      console.error(`particleAbilityTest ConnectAbility onFailed errCode: ${code}`);
    },
  },
);

particleAbility.disconnectAbility(connId, (err) => {
  console.error(`particleAbilityTest disconnectAbility err: ${JSON.stringify(err)}`);
});
```


## disconnectAbility

```TypeScript
function disconnectAbility(connection: number): Promise<void>
```

Disconnects this ability from a specific ServiceAbility. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-particleAbility-function disconnectAbility(connection: number): Promise<void>--><!--Device-particleAbility-function disconnectAbility(connection: number): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| connection | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## Examples

```TypeScript
import { particleAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

let connId = particleAbility.connectAbility(
  {
    bundleName: 'com.ix.ServiceAbility',
    abilityName: 'ServiceAbilityA',
  },
  {
    onConnect: (element, remote) => {
      console.info(`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}`);
    },
    onDisconnect: (element) => {
      console.info(`ConnectAbility onDisconnect element.deviceId: ${element.deviceId}`);
    },
    onFailed: (code) => {
      console.error(`particleAbilityTest ConnectAbility onFailed errCode: ${code}`);
    },
  },
);

particleAbility.disconnectAbility(connId).then(() => {
  console.info('disconnectAbility success');
}).catch((error: BusinessError) => {
  console.error(`particleAbilityTest result errCode : ${error.code}`);
});
```
