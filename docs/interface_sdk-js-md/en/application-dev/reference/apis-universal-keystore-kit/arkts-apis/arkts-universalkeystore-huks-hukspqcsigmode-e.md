# HuksPQCSigMode

```TypeScript
export enum HuksPQCSigMode
```

Enumeration of signature modes for Post-Quantum Cryptography (PQC) algorithms.

**Since:** 26.1.0

<!--Device-huks-export enum HuksPQCSigMode--><!--Device-huks-export enum HuksPQCSigMode-End-->

**System capability:** SystemCapability.Security.Huks.Core

## HUKS_PQC_SIG_MODE_EXTERNAL_MU

```TypeScript
HUKS_PQC_SIG_MODE_EXTERNAL_MU = 2
```

External Mu mode: accepts a pre-computed 64-byte message representative Mu as input.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-HuksPQCSigMode-HUKS_PQC_SIG_MODE_EXTERNAL_MU = 2--><!--Device-HuksPQCSigMode-HUKS_PQC_SIG_MODE_EXTERNAL_MU = 2-End-->

**System capability:** SystemCapability.Security.Huks.Core

## HUKS_PQC_SIG_MODE_PREHASH

```TypeScript
HUKS_PQC_SIG_MODE_PREHASH = 1
```

Pre-hash mode: hashes the message before signing.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-HuksPQCSigMode-HUKS_PQC_SIG_MODE_PREHASH = 1--><!--Device-HuksPQCSigMode-HUKS_PQC_SIG_MODE_PREHASH = 1-End-->

**System capability:** SystemCapability.Security.Huks.Core

## HUKS_PQC_SIG_MODE_PURE

```TypeScript
HUKS_PQC_SIG_MODE_PURE = 0
```

Pure mode: signs the original message directly without pre-hashing.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-HuksPQCSigMode-HUKS_PQC_SIG_MODE_PURE = 0--><!--Device-HuksPQCSigMode-HUKS_PQC_SIG_MODE_PURE = 0-End-->

**System capability:** SystemCapability.Security.Huks.Core
