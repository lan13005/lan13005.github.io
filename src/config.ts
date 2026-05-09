export const site = {
  name: 'Lawrence Ng',
  role: 'Postdoctoral Fellow · Physics & ML',
  greeting: "Hello! I'm Lawrence.",
  tagline: 'Bridging experimental physics and production-grade ML.',
  bio: "Experienced researcher with a Ph.D. in Physics specializing in advanced statistical modeling, data analysis, and machine learning. Proven expertise developing robust, scalable analysis frameworks in Python and C++. Proficient in high-performance computing, parallel processing, and leveraging interdisciplinary collaborations to deliver data-driven solutions.",
  ctas: {
    primary: { label: 'View Projects', href: '/projects' },
    secondary: { label: 'Download CV', href: '/cv.pdf' },
  },
  socials: [
    { kind: 'github', href: 'https://github.com/lan13005', label: 'GitHub' },
    {
      kind: 'linkedin',
      href: 'https://linkedin.com/in/lawrence-ng-070050157',
      label: 'LinkedIn',
    },
    {
      kind: 'scholar',
      href: 'https://scholar.google.com/citations?user=fiWazGQAAAAJ&hl=en',
      label: 'Google Scholar',
    },
    { kind: 'email', href: 'mailto:lng1492@gmail.com', label: 'Email' },
  ],
  whatIDo: [
    {
      icon: 'lucide:flask-conical',
      title: 'Research',
      blurb: 'Statistical modeling and ML for experimental physics analysis.',
    },
    {
      icon: 'lucide:wrench',
      title: 'Engineering',
      blurb: 'Scalable frameworks in Python, C++, and JAX — from prototype to production.',
    },
    {
      icon: 'lucide:git-branch',
      title: 'Open Source',
      blurb: 'Building and maintaining physics analysis tooling used by collaborations.',
    },
  ],
  meta: {
    title: 'Lawrence Ng — Postdoctoral Fellow',
    description:
      'Personal site of Lawrence Ng, a physicist and ML researcher at Thomas Jefferson National Accelerator Facility.',
    ogImage: '/og-image.svg',
  },
};
