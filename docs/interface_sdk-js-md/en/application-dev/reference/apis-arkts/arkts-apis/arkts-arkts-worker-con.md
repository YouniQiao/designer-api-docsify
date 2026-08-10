# Constants

## parentPort

```TypeScript
const parentPort: DedicatedWorkerGlobalScope
```

Worker线程用于与宿主线程通信的对象。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.worker.workerPort

<!--Device-worker-const parentPort: DedicatedWorkerGlobalScope--><!--Device-worker-const parentPort: DedicatedWorkerGlobalScope-End-->

**System capability:** SystemCapability.Utils.Lang

## workerPort

```TypeScript
const workerPort: ThreadWorkerGlobalScope
```

Worker线程用于与宿主线程通信的对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-worker-const workerPort: ThreadWorkerGlobalScope--><!--Device-worker-const workerPort: ThreadWorkerGlobalScope-End-->

**System capability:** SystemCapability.Utils.Lang

