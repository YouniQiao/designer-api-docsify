# ScriptItem

Defines the contents of the JavaScript to be injected.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface ScriptItem--><!--Device-unnamed-export declare interface ScriptItem-End-->

**System capability:** SystemCapability.Web.Webview.Core

## script

```TypeScript
script: string
```

Sets the JavaScript to be injected.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ScriptItem-script: string--><!--Device-ScriptItem-script: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## scriptRules

```TypeScript
scriptRules: Array<string>
```

Sets the rules of the JavaScript.

**Type:** Array&lt;string&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ScriptItem-scriptRules: Array<string>--><!--Device-ScriptItem-scriptRules: Array<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## urlRegexRules

```TypeScript
urlRegexRules?: Array<UrlRegexRule>
```

Set the regular expression rule that allows execution of this JavaScript.

**Type:** Array&lt;[UrlRegexRule](arkts-na-web-urlregexrule-i.md)&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScriptItem-urlRegexRules?: Array<UrlRegexRule>--><!--Device-ScriptItem-urlRegexRules?: Array<UrlRegexRule>-End-->

**System capability:** SystemCapability.Web.Webview.Core

