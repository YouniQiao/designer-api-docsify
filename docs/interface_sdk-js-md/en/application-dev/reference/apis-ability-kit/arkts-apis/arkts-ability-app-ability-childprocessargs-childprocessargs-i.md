# ChildProcessArgs

传递到子进程的参数。[childProcessManager](arkts-app-ability-childprocessmanager.md)启动子进程时，可以通过ChildProcessArgs传递参数到子进程中。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface ChildProcessArgs--><!--Device-unnamed-export interface ChildProcessArgs-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { ChildProcessArgs } from 'kits/@kit.AbilityKit';
```

## entryParams

```TypeScript
entryParams?: string
```

开发者自定义参数，透传到子进程中。可以在[ChildProcess.onStart](arkts-ability-app-ability-childprocess-childprocess-c.md#onstart)方法中通过args.entryParams获取，entryParams支持传输的最大数据量为150KB。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChildProcessArgs-entryParams?: string--><!--Device-ChildProcessArgs-entryParams?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## fds

```TypeScript
fds?: Record<string, int>
```

文件描述符句柄集合，用于主进程和子进程通信，通过key-value的形式传入到子进程中，其中key为自定义字符串，value为文件描述符句柄。可以在  
[ChildProcess.onStart](arkts-ability-app-ability-childprocess-childprocess-c.md#onstart)方法中通过args.fds获取fd句柄。

&lt;b&gt;说明：&lt;/b&gt; 

- fds最多支持16组，每组key的最大长度为20字符。  
- 传递到子进程中句柄数字可能会变，但是指向的文件是一致的。

**Type:** ArkTS-Dyn: [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, number&gt;  <br>ArkTS-Sta：[Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, int&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChildProcessArgs-fds?: Record<string, int>--><!--Device-ChildProcessArgs-fds?: Record<string, int>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

