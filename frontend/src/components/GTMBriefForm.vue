<template>
  <div class="gtm-form">
    <!-- Section 01: Product -->
    <div class="form-section">
      <div class="section-label">01 / Product</div>

      <div class="field-group">
        <label class="field-label">Product Name <span class="required">*</span></label>
        <input
          v-model="form.productName"
          type="text"
          class="field-input"
          :class="{ error: errors.productName }"
          placeholder="e.g. Acme AI SDR"
          @blur="touchField('productName')"
        />
        <span v-if="errors.productName" class="field-error">{{ errors.productName }}</span>
      </div>

      <div class="field-group">
        <label class="field-label">Product Description <span class="required">*</span></label>
        <textarea
          v-model="form.productDescription"
          class="field-input field-textarea"
          :class="{ error: errors.productDescription }"
          placeholder="// What does your product do? Who is it for? What makes it different?"
          rows="3"
          @blur="touchField('productDescription')"
        />
        <span v-if="errors.productDescription" class="field-error">{{ errors.productDescription }}</span>
      </div>

      <div class="field-group">
        <label class="field-label">Pricing Model <span class="required">*</span></label>
        <input
          v-model="form.pricingModel"
          type="text"
          class="field-input"
          :class="{ error: errors.pricingModel }"
          placeholder="e.g. $500/mo per seat, usage-based, freemium"
          @blur="touchField('pricingModel')"
        />
        <span v-if="errors.pricingModel" class="field-error">{{ errors.pricingModel }}</span>
      </div>
    </div>

    <!-- Section 02: Buyer -->
    <div class="form-section">
      <div class="section-label">02 / Buyer</div>

      <div class="field-group">
        <label class="field-label">Ideal Customer Profile (ICP) <span class="required">*</span></label>
        <textarea
          v-model="form.icp"
          class="field-input field-textarea"
          :class="{ error: errors.icp }"
          placeholder="// B2B SaaS companies, 10–200 employees, sales team of 3–10, Series A or bootstrapped..."
          rows="3"
          @blur="touchField('icp')"
        />
        <span v-if="errors.icp" class="field-error">{{ errors.icp }}</span>
      </div>

      <div class="field-group">
        <label class="field-label">Target Market <span class="required">*</span></label>
        <input
          v-model="form.targetMarket"
          type="text"
          class="field-input"
          :class="{ error: errors.targetMarket }"
          placeholder="e.g. US, SMB SaaS founders and VP Sales"
          @blur="touchField('targetMarket')"
        />
        <span v-if="errors.targetMarket" class="field-error">{{ errors.targetMarket }}</span>
      </div>
    </div>

    <!-- Section 03: GTM Strategy -->
    <div class="form-section">
      <div class="section-label">03 / GTM Strategy</div>

      <div class="field-row">
        <div class="field-group half">
          <label class="field-label">Sales Channel <span class="required">*</span></label>
          <select
            v-model="form.salesChannel"
            class="field-input field-select"
            :class="{ error: errors.salesChannel }"
            @blur="touchField('salesChannel')"
          >
            <option value="" disabled>Select channel...</option>
            <option value="outbound_email">Outbound Email</option>
            <option value="linkedin">LinkedIn</option>
            <option value="cold_call">Cold Call</option>
            <option value="plg">Product-Led Growth</option>
            <option value="inbound">Inbound / Content</option>
            <option value="partnerships">Partnerships</option>
          </select>
          <span v-if="errors.salesChannel" class="field-error">{{ errors.salesChannel }}</span>
        </div>

        <div class="field-group half">
          <label class="field-label">GTM Goal <span class="required">*</span></label>
          <select
            v-model="form.gtmGoal"
            class="field-input field-select"
            :class="{ error: errors.gtmGoal }"
            @blur="touchField('gtmGoal')"
          >
            <option value="" disabled>Select goal...</option>
            <option value="first_10_customers">Land first 10 customers</option>
            <option value="expand_segment">Expand existing segment</option>
            <option value="new_market">Enter new market</option>
            <option value="reactivate_churned">Reactivate churned customers</option>
          </select>
          <span v-if="errors.gtmGoal" class="field-error">{{ errors.gtmGoal }}</span>
        </div>
      </div>

      <div class="field-group">
        <label class="field-label">Main Pain Point <span class="required">*</span></label>
        <textarea
          v-model="form.painPoint"
          class="field-input field-textarea"
          :class="{ error: errors.painPoint }"
          placeholder="// SDRs spend 70% of time on research and list building..."
          rows="3"
          @blur="touchField('painPoint')"
        />
        <span v-if="errors.painPoint" class="field-error">{{ errors.painPoint }}</span>
      </div>

      <div class="field-group">
        <label class="field-label">Competitors <span class="field-hint">(comma-separated)</span></label>
        <input
          v-model="form.competitors"
          type="text"
          class="field-input"
          placeholder="Apollo, Outreach, Clay"
        />
      </div>
    </div>

    <!-- Section 04: Optional -->
    <div class="form-section optional-section">
      <div class="section-label">
        04 / Optional
        <button class="toggle-optional" @click="showOptional = !showOptional" type="button">
          {{ showOptional ? '▲ hide' : '▼ show' }}
        </button>
      </div>

      <div v-if="showOptional" class="optional-fields">
        <div class="field-row">
          <div class="field-group half">
            <label class="field-label">Company Stage</label>
            <input v-model="form.companyStage" type="text" class="field-input" placeholder="Pre-seed, Seed, Series A..." />
          </div>
          <div class="field-group half">
            <label class="field-label">Team Size</label>
            <input v-model="form.teamSize" type="text" class="field-input" placeholder="e.g. 8 people, solo founder" />
          </div>
        </div>

        <div class="field-group">
          <label class="field-label">Existing GTM Problems</label>
          <textarea v-model="form.existingProblems" class="field-input field-textarea" placeholder="// What's broken or missing in your current GTM?" rows="2" />
        </div>

        <div class="field-group">
          <label class="field-label">Current Outreach Strategy</label>
          <textarea v-model="form.outreachStrategy" class="field-input field-textarea" placeholder="// What have you already tried?" rows="2" />
        </div>
      </div>
    </div>

    <!-- Submit -->
    <div class="form-submit">
      <div v-if="submitAttempted && globalErrors.length" class="global-error">
        {{ globalErrors.length }} field{{ globalErrors.length > 1 ? 's' : '' }} need attention above.
      </div>
      <button class="submit-btn" :disabled="loading" @click="handleSubmit">
        <span v-if="!loading">Run GTM Simulation →</span>
        <span v-else>Building simulation...</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import { validateGTMBrief, formatGTMBrief } from '../utils/gtmFormatter.js'

const props = defineProps({
  loading: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['submit'])

const showOptional = ref(false)
const submitAttempted = ref(false)
const touched = reactive({})

const form = reactive({
  productName: '',
  productDescription: '',
  pricingModel: '',
  icp: '',
  targetMarket: '',
  salesChannel: '',
  gtmGoal: '',
  painPoint: '',
  competitors: '',
  companyStage: '',
  teamSize: '',
  existingProblems: '',
  outreachStrategy: '',
})

const allErrors = computed(() => {
  const errs = validateGTMBrief(form)
  const map = {}
  for (const e of errs) map[e.field] = e.message
  return map
})

const errors = computed(() => {
  const visible = {}
  for (const [field, msg] of Object.entries(allErrors.value)) {
    if (submitAttempted.value || touched[field]) {
      visible[field] = msg
    }
  }
  return visible
})

const globalErrors = computed(() => Object.values(allErrors.value))

function touchField(field) {
  touched[field] = true
}

function handleSubmit() {
  submitAttempted.value = true
  if (globalErrors.value.length > 0) return
  emit('submit', formatGTMBrief(form))
}
</script>

<style scoped>
.gtm-form {
  display: flex;
  flex-direction: column;
  gap: 0;
}

/* Sections */
.form-section {
  border: 1px solid #E0E0E0;
  border-bottom: none;
  padding: 16px 20px;
  background: #fff;
}

.form-section:last-of-type {
  border-bottom: 1px solid #E0E0E0;
}

.optional-section {
  background: #FAFAFA;
}

.section-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: #999;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}

/* Fields */
.field-group {
  margin-bottom: 12px;
}

.field-group:last-child {
  margin-bottom: 0;
}

.field-group.half {
  flex: 1;
  min-width: 0;
}

.field-row {
  display: flex;
  gap: 12px;
  margin-bottom: 12px;
}

.field-label {
  display: block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 600;
  color: #333;
  margin-bottom: 4px;
  letter-spacing: 0.3px;
}

.field-hint {
  font-weight: 400;
  color: #999;
  margin-left: 4px;
}

.required {
  color: #FF5722;
}

.field-input {
  width: 100%;
  box-sizing: border-box;
  background: #fff;
  border: 1px solid #D0D0D0;
  border-radius: 3px;
  padding: 8px 10px;
  font-family: 'Space Grotesk', system-ui, sans-serif;
  font-size: 13px;
  color: #111;
  outline: none;
  transition: border-color 0.15s;
  -webkit-appearance: none;
}

.field-input:focus {
  border-color: #000;
}

.field-input.error {
  border-color: #E53935;
}

.field-input::placeholder {
  color: #AAA;
  font-style: italic;
}

.field-textarea {
  resize: vertical;
  min-height: 60px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  line-height: 1.5;
}

.field-select {
  cursor: pointer;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%23666'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 10px center;
  padding-right: 28px;
}

.field-error {
  display: block;
  font-size: 11px;
  color: #E53935;
  margin-top: 3px;
  font-family: 'JetBrains Mono', monospace;
}

/* Optional toggle */
.toggle-optional {
  background: none;
  border: none;
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  color: #888;
  cursor: pointer;
  padding: 0;
  letter-spacing: 0.5px;
}

.toggle-optional:hover {
  color: #333;
}

.optional-fields {
  margin-top: 4px;
}

/* Submit area */
.form-submit {
  padding: 16px 0 0;
}

.global-error {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: #E53935;
  margin-bottom: 10px;
}

.submit-btn {
  width: 100%;
  padding: 12px 20px;
  background: #000;
  color: #fff;
  border: 1px solid #000;
  border-radius: 3px;
  font-family: 'Space Grotesk', system-ui, sans-serif;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.3px;
  cursor: pointer;
  transition: background 0.15s, transform 0.1s;
}

.submit-btn:hover:not(:disabled) {
  background: #FF5722;
  border-color: #FF5722;
}

.submit-btn:active:not(:disabled) {
  transform: translateY(1px);
}

.submit-btn:disabled {
  background: #CCC;
  border-color: #CCC;
  cursor: not-allowed;
}
</style>
