task 'a2' => 'a2.pdf'
task 'a5' => 'a5.pdf'
rule '.pdf' => '.md' do |t|
  sh "pandoc #{t.source} -o #{t.name}"
end
