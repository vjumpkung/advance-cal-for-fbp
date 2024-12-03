var F=Object.defineProperty;var W=(e,o,s)=>o in e?F(e,o,{enumerable:!0,configurable:!0,writable:!0,value:s}):e[o]=s;var y=(e,o,s)=>W(e,typeof o!="symbol"?o+"":o,s);import{r as h,a as A}from"./vendor-8C3hFYWf.js";import{F as B}from"./file-saver-CwgoR5c5.js";import{H as G}from"./react-helmet-DQClQlXB.js";import{B as _,Q as M}from"./react-toastify-CktzUeMi.js";import{z as t}from"./zod-DXqQCM1T.js";import{L as V,a as C,b as H,c as $}from"./@comfyorg/litegraph-06-xkOGy.js";import{a as q}from"./axios-DXsv3KKR.js";(function(){const o=document.createElement("link").relList;if(o&&o.supports&&o.supports("modulepreload"))return;for(const n of document.querySelectorAll('link[rel="modulepreload"]'))r(n);new MutationObserver(n=>{for(const i of n)if(i.type==="childList")for(const c of i.addedNodes)c.tagName==="LINK"&&c.rel==="modulepreload"&&r(c)}).observe(document,{childList:!0,subtree:!0});function s(n){const i={};return n.integrity&&(i.integrity=n.integrity),n.referrerPolicy&&(i.referrerPolicy=n.referrerPolicy),n.crossOrigin==="use-credentials"?i.credentials="include":n.crossOrigin==="anonymous"?i.credentials="omit":i.credentials="same-origin",i}function r(n){if(n.ep)return;n.ep=!0;const i=s(n);fetch(n.href,i)}})();var P={exports:{}},N={};/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */var U=h,J=Symbol.for("react.element"),D=Symbol.for("react.fragment"),Z=Object.prototype.hasOwnProperty,K=U.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner,Q={key:!0,ref:!0,__self:!0,__source:!0};function R(e,o,s){var r,n={},i=null,c=null;s!==void 0&&(i=""+s),o.key!==void 0&&(i=""+o.key),o.ref!==void 0&&(c=o.ref);for(r in o)Z.call(o,r)&&!Q.hasOwnProperty(r)&&(n[r]=o[r]);if(e&&e.defaultProps)for(r in o=e.defaultProps,o)n[r]===void 0&&(n[r]=o[r]);return{$$typeof:J,type:e,key:i,ref:c,props:n,_owner:K.current}}N.Fragment=D;N.jsx=R;N.jsxs=R;P.exports=N;var a=P.exports,T,E=A;T=E.createRoot,E.hydrateRoot;const S=t.union([t.number().int(),t.string()]),z=t.union([t.object({0:t.number(),1:t.number()}).passthrough().transform(e=>[e[0],e[1]]),t.tuple([t.number(),t.number()])]),X=t.object({collapsed:t.boolean().optional(),pinned:t.boolean().optional(),allow_interaction:t.boolean().optional(),horizontal:t.boolean().optional(),skip_repeated_outputs:t.boolean().optional()}).passthrough(),k=t.union([t.string(),t.array(t.string()),t.number()]),j=t.union([t.number().int(),t.string().transform(e=>parseInt(e)).refine(e=>!isNaN(e),{message:"Invalid number"})]),Y=t.object({name:t.string(),type:k,link:t.number().nullable().optional(),slot_index:j.optional()}).passthrough(),ee=t.object({name:t.string(),type:k,links:t.array(t.number()).nullable().optional(),slot_index:j.optional()}).passthrough(),te=t.object({"Node name for S&R":t.string().optional()}).passthrough(),oe=t.union([t.array(t.any()),t.record(t.any())]),re=t.object({id:S,type:t.string(),pos:z,size:z,flags:X,order:t.number(),mode:t.number(),inputs:t.array(Y).optional(),outputs:t.array(ee).optional(),properties:te,widgets_values:oe.optional(),color:t.string().optional(),bgcolor:t.string().optional()}).passthrough(),se=t.tuple([t.number(),S,j,S,j,k]),ne=t.object({title:t.string(),bounding:t.tuple([t.number(),t.number(),t.number(),t.number()]),color:t.string().optional(),font_size:t.number().optional(),locked:t.boolean().optional()}).passthrough(),ie=t.object({links_ontop:t.boolean().optional(),align_to_grid:t.boolean().optional()}).passthrough(),ae=t.object({last_node_id:t.number(),last_link_id:t.number(),nodes:t.array(re),links:t.array(se),groups:t.array(ne).optional(),config:ie.optional().nullable(),version:t.number()});function le(e){try{const o=JSON.parse(e),s=ae.parse(o);return console.log("Validation successful:",s),s}catch(o){throw o instanceof t.ZodError?console.error("Validation error:",o.errors):console.error("Parsing error:",o),Error(o)}}const ue=(e,o,s)=>{var n;const r=(n=s.target.files)==null?void 0:n[0];if(r&&o){const i=new FileReader;return i.onload=c=>{var p;try{const l=(p=c.target)==null?void 0:p.result,d=le(l);console.log(d),o.clear(),o.configure(d),e&&(e.value=""),_.success("Loading Workflow Success",{position:"top-right",autoClose:5e3,hideProgressBar:!0,closeOnClick:!0,pauseOnHover:!0,draggable:!0,progress:void 0,theme:"dark",style:{marginTop:"1.25em"}})}catch{_.error("Error loading workflow file. Please ensure it is a valid workflow.",{position:"top-right",autoClose:5e3,hideProgressBar:!0,closeOnClick:!0,pauseOnHover:!0,draggable:!0,progress:void 0,theme:"dark",style:{marginTop:"1.25em"}})}},i.onerror=()=>{_.error("Error reading file",{position:"top-right",autoClose:5e3,hideProgressBar:!0,closeOnClick:!0,pauseOnHover:!0,draggable:!0,progress:void 0,theme:"dark",style:{marginTop:"1.25em"}})},i.readAsText(r),r.name}};function ce({graph:e,canvas:o}){const s=h.useRef(null),[r,n]=h.useState(!1),[i,c]=h.useState(!0),[p,l]=h.useState(null),[d,g]=h.useState("untitled"),u=()=>{var f;(f=s.current)==null||f.click()},b=()=>{if(e){const f=JSON.stringify(e.serialize()),w=new Blob([f],{type:"text/plain;charset=utf-8"}),O=prompt("Enter Filename : ",`workflow-${Date.now()}`);if(O===null)return;B.saveAs(w,`${O}.json`),l(e.asSerialisable()),g(O)}},m=()=>{e&&confirm("Clear workflow?")&&(e.clear(),_.info("Workflow Cleared",{position:"top-right",autoClose:5e3,hideProgressBar:!0,closeOnClick:!0,pauseOnHover:!0,draggable:!0,progress:void 0,theme:"dark",style:{marginTop:"1.25em"}}),g("untitled"),o.ds.offset=[0,0],o.setZoom(1,[0,0]),o.setDirty(!0,!0))},x=()=>{e&&(r?(e.stop(),n(!1)):(e.start(),n(!0)))};return a.jsxs(a.Fragment,{children:[a.jsx(G,{children:a.jsxs("title",{children:[i?"":"*",d+" ","- AdvFBP"]})}),a.jsxs("div",{className:"topbar",children:[a.jsxs("div",{className:"leftmenu",children:[a.jsxs("button",{className:"buttonmenu",onClick:b,children:[a.jsx("i",{className:"pi pi-save"})," Save"]}),a.jsxs("button",{className:"buttonmenu",onClick:u,children:[a.jsx("i",{className:"pi pi-upload"})," Load"]}),a.jsx("input",{type:"file",ref:s,onChange:f=>{const w=ue(s.current,e,f);w&&g(w.split(".")[0])},accept:".json",style:{display:"none"}}),a.jsxs("button",{className:"buttonmenu",onClick:m,children:[a.jsx("i",{className:"pi pi-eraser"})," Clear"]})]}),a.jsx("div",{className:"rightmenu",children:a.jsx("button",{className:"buttonmenu",onClick:x,children:r?a.jsxs("span",{children:[a.jsx("i",{className:"pi pi-stop"})," Stop"]}):a.jsxs("span",{children:[a.jsx("i",{className:"pi pi-play"})," Start"]})})})]})]})}async function de(){const e=await q.get("/api/object_info");if(e.status===200)return e.data}function I(e,o){let s=e[1].default,{min:r,max:n,step:i}=e[1];return s==null&&(s=0),r==null&&(r=Number.MIN_SAFE_INTEGER),n==null&&(n=Number.MAX_SAFE_INTEGER),i==null&&(i=o),e[1].min=r,e[1].max=n,e[1].step=1*i,{val:s,config:{...e[1]}}}function L(e){return e==="slider"?"slider":"number"}function pe(e,o,s){const r=document.createElement("textarea");r.className="comfy-multiline-input",r.value=s.defaultVal,r.placeholder=s.placeholder||o;const n=e.addDOMWidget(o,"customtext",r,{getValue(){return r.value},setValue(i){r.value=i}});return n.inputEl=r,r.addEventListener("input",()=>{var i;(i=n.callback)==null||i.call(n,n.value)}),{minWidth:400,minHeight:200,widget:n}}const v={FLOAT(e,o,s){let r=L(s[1].display),{val:n,config:i}=I(s,.5);return{widget:e.addWidget(r,o,n,()=>{},i)}},INT(e,o,s){let r=L(s[1].display);const{val:n,config:i}=I(s,1);return Object.assign(i,{precision:0}),{widget:e.addWidget(r,o,n,function(c){const p=this.options.step/10;this.value=Math.round(c/p)*p},i)}},BOOLEAN(e,o,s){let r=s[1].default;return{widget:e.addWidget("toggle",o,r,()=>{},{on:s[1].label_on,off:s[1].label_off})}},STRING(e,o,s){const r=s[1].default||"",n=!!s[1].multiline;let i;return n?i={widget:pe(e,o,{defaultVal:r,...s[1]})}:i={widget:e.addWidget("text",o,r,()=>{},{})},s[1].dynamicPrompts!=null&&(i.widget.dynamicPrompts=s[1].dynamicPrompts),i},COMBO(e,o,s){const r=s[0];let n=r[0];return s[1]&&s[1].default&&(n=s[1].default),{widget:e.addWidget("combo",o,n,()=>{},{values:r})}}};async function fe(e){var o;for(const s in e){const r=e[s],n=(o=class extends V{constructor(c){var g;super(c),r.input.required;var p=r.input.required;r.input.optional!=null&&(p=Object.assign({},r.input.required,r.input.optional));const l={minWidth:1,minHeight:1};for(const u in p){const b=p[u],m=b[0],x=b[1]??{},f=[m,x];(g=f[1])!=null&&g.forceInput?this.addInput(u,m):Array.isArray(m)?Object.assign(l,v.COMBO(this,u,f)||{}):`${m}:${u}`in v?Object.assign(l,v[`${m}:${u}`](this,u,f)||{}):m in v?Object.assign(l,v[m](this,u,f)||{}):this.addInput(u,m)}for(const u in r.output){let b=r.output[u];b instanceof Array&&(b="COMBO");const m=r.output_name[u]||b,f=r.output_is_list[u]?{shape:C.GRID_SHAPE}:{};this.addOutput(m,b,f)}const d=this.computeSize();d[0]=Math.max(l.minWidth,d[0]*1.5),d[1]=Math.max(l.minHeight,d[1]),this.size=d,this.serialize_widgets=!0}configure(c){const p=(l,d)=>{const g={...d};if(l.widget===void 0&&d.widget!==void 0)return this.inputs.push(l),d;for(const u of["name","type","shape"])l[u]!==void 0&&(g[u]=l[u]);return g};for(const l of["inputs","outputs"]){const d=c[l]??[];c[l]=d.map((g,u)=>p(this[l][u]??{},g))}super.configure(c)}},y(o,"comfyClass",r.name),y(o,"title",r.display_name||r.name),y(o,"nodeData",r),y(o,"category"),o);n.comfyClass=r.name,C.registerNodeType(s,n),n.category=r.category}}async function me(e,o,s){const r=new H,n=new $(e,r);function i(){const p=Math.max(window.devicePixelRatio,1),{width:l,height:d}=e.getBoundingClientRect();e.width=Math.round(l*p),e.height=Math.round(d*p),e.getContext("2d").scale(p,p),n.draw(!0,!0)}i(),window.addEventListener("resize",i),o(r),s(n);const c=await de();await fe(c)}function ge({setGraph:e,setCanvas:o,canvasRef:s}){h.useEffect(()=>{s.current&&me(s.current,e,o)},[])}function he(){const e=h.useRef(null),[o,s]=h.useState(void 0),[r,n]=h.useState(void 0);return ge({setGraph:s,setCanvas:n,canvasRef:e}),a.jsxs(a.Fragment,{children:[a.jsx(ce,{graph:o,canvas:r}),a.jsx("canvas",{style:{position:"absolute",zIndex:0},ref:e,id:"graph-canvas"})]})}T(document.getElementById("root")).render(a.jsxs(h.StrictMode,{children:[a.jsx(he,{}),a.jsx(M,{})]}));
