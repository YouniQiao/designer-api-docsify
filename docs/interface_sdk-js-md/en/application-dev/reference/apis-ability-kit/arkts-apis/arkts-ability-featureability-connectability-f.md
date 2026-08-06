# connectAbility

## connectAbility

```TypeScript
function connectAbility(request: Want, options: ConnectOptions): number
```

Connects this ability to a ServiceAbility.
    **NOTE**  
    
    For details about the startup rules for the components in the FA model, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.  
        To connect to a ServiceAbility of another application, the target application must be configured with  
    associated startup (**AssociateWakeUp** set to **true**).

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-featureAbility-function connectAbility(request: Want, options: ConnectOptions): number--><!--Device-featureAbility-function connectAbility(request: Want, options: ConnectOptions): number-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | ServiceAbility to connect. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Connection options. |

**Return value:**

| Type | Description |
| --- | --- |
| number | ID of the connected ServiceAbility. The ID starts from 0 and is incremented by 1 each time a connection is set up. |

**Example**

```TypeScript
import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

let connectId = featureAbility.connectAbility(
  {
    deviceId: '',
    bundleName: 'com.ix.ServiceAbility',
    abilityName: 'com.ix.ServiceAbility.ServiceAbilityA',
  },
  {
    onConnect: (element, remote) => {
      console.info(`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}`);
    },
    onDisconnect: (element) => {
      console.info(`ConnectAbility onDisconnect element.deviceId : ${element.deviceId}`);
    },
    onFailed: (code) => {
      console.error(`featureAbilityTest ConnectAbility onFailed errCode : ${code}`);
    },
  },
);
```

