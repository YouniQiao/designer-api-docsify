# Participant (System API)

端云共享的参与者。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-sharing-interface Participant--><!--Device-sharing-interface Participant-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudData } from 'kits/@kit.ArkData';
```

## attachInfo

```TypeScript
attachInfo?: string
```

附加信息，用于扩展额外的参与者信息。如用于参与者身份校验的校验码等，默认为空字符串。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Participant-attachInfo?: string--><!--Device-Participant-attachInfo?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## identity

```TypeScript
identity: string
```

参与者的ID。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Participant-identity: string--><!--Device-Participant-identity: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## privilege

```TypeScript
privilege?: Privilege
```

指定的共享数据权限。默认为Privilege的默认值。

**Type:** [Privilege](arkts-arkdata-sharing-privilege-i-sys.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Participant-privilege?: Privilege--><!--Device-Participant-privilege?: Privilege-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## role

```TypeScript
role?: Role
```

参与者的角色，为邀请者或被邀请者。默认为undefined。

**Type:** [Role](../../apis-ability-kit/arkts-apis/arkts-ability-abilitytoolaccessctrl-role-e-sys.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Participant-role?: Role--><!--Device-Participant-role?: Role-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## state

```TypeScript
state?: State
```

共享的状态。默认为undefined。

**Type:** [State](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-state-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Participant-state?: State--><!--Device-Participant-state?: State-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

