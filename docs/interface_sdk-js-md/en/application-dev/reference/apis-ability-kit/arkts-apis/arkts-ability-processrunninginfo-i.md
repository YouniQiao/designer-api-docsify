# ProcessRunningInfo

运行进程信息，可以通过appManager中  
[getProcessRunningInfos](arkts-ability-appmanager-getprocessrunninginfos-depr-f.md#getprocessrunninginfos)方法来获取运行进程信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ProcessInformation/ProcessInformation

<!--Device-unnamed-export interface ProcessRunningInfo--><!--Device-unnamed-export interface ProcessRunningInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

## bundleNames

```TypeScript
bundleNames: Array<string>
```

进程中所有运行的Bundle名称。

**Type:** Array&lt;string&gt;

**Default:** an array of the bundleNames running in the process

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [ProcessInformation:ProcessInformation.bundleNames](arkts-ability-processinformation-i.md#bundlenames)

<!--Device-ProcessRunningInfo-bundleNames: Array<string>--><!--Device-ProcessRunningInfo-bundleNames: Array<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

## pid

```TypeScript
pid: number
```

进程ID。

**Type:** number

**Default:** process id

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [ProcessInformation:ProcessInformation.pid](arkts-ability-processinformation-i.md#pid)

<!--Device-ProcessRunningInfo-pid: number--><!--Device-ProcessRunningInfo-pid: number-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

## processName

```TypeScript
processName: string
```

进程名称。

**Type:** string

**Default:** the name of the process

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [ProcessInformation:ProcessInformation.processName](arkts-ability-processinformation-i.md#processname)

<!--Device-ProcessRunningInfo-processName: string--><!--Device-ProcessRunningInfo-processName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

## uid

```TypeScript
uid: number
```

应用程序的UID。

**Type:** number

**Default:** user id

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [ProcessInformation:ProcessInformation.uid](arkts-ability-processinformation-i.md#uid)

<!--Device-ProcessRunningInfo-uid: number--><!--Device-ProcessRunningInfo-uid: number-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

