# abort

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## abort

```TypeScript
function abort(): void
```

该方法会导致进程立即退出并生成一个核心文件，谨慎使用。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-process-function abort(): void--><!--Device-process-function abort(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## Examples

```TypeScript
process.abort();
```

